from .libs import re, sys, logging, asyncio

from .task_api import *
from .send import CreateSend


class CreateTask(CreateSend):
    def __init__(self, log_path, headers, cookies):
        super().__init__()

        self.headers = headers
        self.cookies = cookies

        config = {
            "level": logging.INFO,
            "format": "%(asctime)s - %(levelname)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "force": True,
        }

        if log_path is not None:
            log_path.parent.mkdir(parents=True, exist_ok=True)  # 建立資料夾
            config.update({"filename": str(log_path), "encoding": "utf-8"})

        logging.basicConfig(**config)
        sys.excepthook = lambda *args: (
            logging.error("Exception", exc_info=args),
            sys.__excepthook__(*args),
        )

    def nikke_input_cdKey(self, data={}):
        # ! 等待研究
        # data['data']['components'][0]['components'][0]['value'] = ""
        # result = self.http_post(DiscordAPI["Nikke-Bot"], self.headers, self.cookies, data)

        cdKey = self.http_get(DiscordAPI["Nikke-CdKeys"], self.headers, self.cookies)

        try:
            data = cdKey.json()
            for data in data:
                content = data["content"]

                # 嘗試取得 Cd-Key, 排除其他類型內容
                if content and re.fullmatch(r'[A-Za-z0-9]+', content):
                    print(content)

        except:
            logging.error(f"Nikke Cd-Key 取得失敗")

    def nikke_discord_signIn(self, data={}):
        signIn = self.http_post(DiscordAPI["Nikke-Bot"], self.headers, self.cookies, data)

        try:
            logging.error(f"Nikke-SignIn: {signIn.json()}")
        except:
            if signIn.text == "":
                logging.info("Nikke-SignIn: 簽到成功")

    def hoyolab_checkIn(self):

        state_parse = {
            "GenshInimpact": lambda retcode: (
                "簽到成功" if retcode == 0 else "已經簽到" if retcode == -5003 else "簽到失敗"
            ),
            "HonkaiStarRail": lambda retcode: (
                "簽到成功" if retcode == 0 else "已經簽到" if retcode == -5003 else "簽到失敗"
            ),
            # "ZenlessZoneZero": lambda retcode: "簽到成功" if retcode == 0 else "已經簽到", # -500012 "已經簽到", -500004 "操作頻繁"
        }

        async def factory():
            works = [
                self.async_http_post(name, url, self.headers, self.cookies)
                for name, url in HoyolabAPI.items()
            ]

            for result in await asyncio.gather(*works):
                state = state_parse.get(result["Name"], lambda *args: result)(result["retcode"])
                logging.info(f"{result['Name']}: {state}")

        asyncio.run(factory())

    def leve_checkIn(self):

        state_parse = {
            "CheckIn": lambda code: (
                "簽到成功"
                if code == 0
                else "已經簽到" if code == 1001009 else "簽到失敗" if code == 300001 else "參數錯誤"
            ),
            "StageCheckIn": lambda code: (
                "簽到成功"
                if code == 0
                else (
                    "已經簽到"
                    if code == 1002007 or code == 1001009
                    else "簽到失敗" if code == 300001 else "參數錯誤"
                )
            ),
        }

        async def factory():
            works = [
                self.async_http_post(name, url, self.headers, self.cookies)
                for name, url in LeveCheckInAPI.items()
            ]

            for result in await asyncio.gather(*works):
                state = state_parse.get(result["Name"], lambda *args: result)(result["code"])
                logging.info(f"{result['Name']}: {state}")

        asyncio.run(factory())

    def leve_state(self):
        ViewPoints = self.http_post(LeveStateAPI["ViewPoints"], self.headers, self.cookies)
        logging.info(f"Points: {ViewPoints.json()['data']['total_points']}")

        task_status = self.http_post(LeveStateAPI["TaskStatus"], self.headers, self.cookies)
        for State in task_status.json()["data"]["tasks"]:
            logging.info(
                f"任務: {State['task_name']} | 代號: {State['task_id']} | 完成: {State['reward_infos'][0]['is_completed']}"
            )
