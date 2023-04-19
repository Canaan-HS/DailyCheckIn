from .__Lib__ import asyncio

from .TaskAPI import *
from .Send import CreateSend

class CreateTask(CreateSend):
    def __init__(self, Headers, Cookies, Data={}):
        super().__init__()

        self.Headers = Headers
        self.Cookies = Cookies
        self.Data = Data

    def LeveCheckIn(self):
        # 簽到成功 [{'name': 'CheckIn', 'code': 0, 'code_type': 0, 'msg': 'ok', 'data': {'status': 1}}, {'name': 'StageCheckIn', 'code': 0, 'code_type': 0, 'msg': 'ok', 'data': {'status': 1}}]
        # 已經簽到 [{'name': 'CheckIn', 'code': 1001009, 'code_type': 1, 'msg': 'system error', 'data': None}, {'name': 'StageCheckIn', 'code': 1002007, 'code_type': 2, 'msg': 'DailyStageCheckIn UserCompleteTaskAndAddPoints error, err=stageTaskAllComplete already sign in today', 'data': None}]
        # code: 300001 代表著失敗

        async def Factory():
            works = [
                self.async_http_post(
                    Name,
                    Work["Url"],
                    {"task_id": Work["ID"]},
                    self.Headers,
                    self.Cookies
                )
                for Name, Work in LeveCheckInAPI.items()
            ]
            results = await asyncio.gather(*works)
            print(results)

        asyncio.run(Factory())

    def LeveState(self):
        ViewPoints = self.http_post(LeveStateAPI["ViewPoints"], self.Headers, self.Cookies)
        print(f"Total Points: {ViewPoints.json()['data']['total_points']}")

        TaskStatus = self.http_post(LeveStateAPI["TaskStatus"], self.Headers, self.Cookies)
        for State in TaskStatus.json()['data']['tasks']:
            print(f"Task: {State['task_name']} | ID: {State['task_id']} | IsCompleted: {State['reward_infos'][0]['is_completed']}")

    def DiscordSignIn(self):
        Discoed = self.http_post(DiscordAPI["SignIn"], self.Headers, self.Cookies, self.Data)

        try:
            print(f"簽到錯誤: {Discoed.json()}")
        except:
            if Discoed.text == "":
                print("簽到成功")