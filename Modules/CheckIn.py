from .__Lib__ import sys, logging, asyncio

from .TaskAPI import *
from .Send import CreateSend

class CreateTask(CreateSend):
    def __init__(self, LogPath, Headers, Cookies, Data={}):
        super().__init__()

        self.Headers = Headers
        self.Cookies = Cookies
        self.Data = Data

        Config = {
            "level": logging.INFO,
            "format": "%(asctime)s - %(levelname)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "force": True
        }

        if LogPath is not None:
            Config.update({
                "filename": str(LogPath),
                "encoding": "utf-8"
            })
 
        logging.basicConfig(**Config)
        sys.excepthook = lambda *args: (
            logging.error("Exception", exc_info=args),
            sys.__excepthook__(*args),
        )

    def DiscordSignIn(self):
        Discoed = self.http_post(DiscordAPI["SignIn"], self.Headers, self.Cookies, self.Data)

        try:
            logging.error(f"Discord: {Discoed.json()}")
        except:
            if Discoed.text == "":
                logging.info("Discord: 簽到成功")

    def HoyolabCheckIn(self):

        StateParse = {
            "GenshInimpact": lambda retcode: "", # -5003
            "HonkaiStarRail": lambda retcode: "", # -5003
            "ZenlessZoneZero": lambda retcode: "", # -500012, -500004
        }

        async def Factory():
            works = [
                self.async_http_post(Name, Url, self.Headers, self.Cookies)
                for Name, Url in HoyolabAPI.items()
            ]

            for result in await asyncio.gather(*works):
                logging.info(result)

        asyncio.run(Factory())

    def LeveCheckIn(self):

        StateParse = {
            "CheckIn": lambda code: "簽到成功" if code == 0 else "已經簽到" if code == 1001009 else "簽到失敗" if code == 300001 else "參數錯誤",
            "StageCheckIn": lambda code: "簽到成功" if code == 0 else "已經簽到" if code == 1002007 else "簽到失敗" if code == 300001 else "參數錯誤",
        }

        async def Factory():
            works = [
                self.async_http_post(Name, Url, self.Headers, self.Cookies)
                for Name, Url in LeveCheckInAPI.items()
            ]

            for result in await asyncio.gather(*works):
                state = StateParse.get(result['Name'], lambda *args: result)(result['code'])
                logging.info(f"{result['Name']}: {state}")

        asyncio.run(Factory())

    def LeveState(self):
        ViewPoints = self.http_post(LeveStateAPI["ViewPoints"], self.Headers, self.Cookies)
        logging.info(f"Points: {ViewPoints.json()['data']['total_points']}")

        TaskStatus = self.http_post(LeveStateAPI["TaskStatus"], self.Headers, self.Cookies)
        for State in TaskStatus.json()['data']['tasks']:
            logging.info(f"任務: {State['task_name']} | 代號: {State['task_id']} | 完成: {State['reward_infos'][0]['is_completed']}")