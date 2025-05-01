from .__Lib__ import re, sys, logging, asyncio

from .TaskAPI import *
from .Send import CreateSend


class CreateTask(CreateSend):
    def __init__(self, LogPath, Headers, Cookies):
        super().__init__()

        self.Headers = Headers
        self.Cookies = Cookies

        Config = {
            "level": logging.INFO,
            "format": "%(asctime)s - %(levelname)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "force": True,
        }

        if LogPath is not None:
            LogPath.parent.mkdir(parents=True, exist_ok=True)  # 建立資料夾
            Config.update({"filename": str(LogPath), "encoding": "utf-8"})

        logging.basicConfig(**Config)
        sys.excepthook = lambda *args: (
            logging.error("Exception", exc_info=args),
            sys.__excepthook__(*args),
        )

    def NikkeInputCdKey(self, Data={}):
        # ! 等待研究
        # Data['data']['components'][0]['components'][0]['value'] = ""
        # result = self.http_post(DiscordAPI["Nikke-Bot"], self.Headers, self.Cookies, Data)

        CdKey = self.http_get(DiscordAPI["Nikke-CdKeys"], self.Headers, self.Cookies)

        try:
            Data = CdKey.json()
            for data in Data:
                content = data["content"]

                # 嘗試取得 Cd-Key, 排除其他類型內容
                if content and re.fullmatch(r'[A-Za-z0-9]+', content):
                    print(content)

        except:
            logging.error(f"Nikke Cd-Key 取得失敗")

    def NikkeDiscordSignIn(self, Data={}):
        SignIn = self.http_post(DiscordAPI["Nikke-Bot"], self.Headers, self.Cookies, Data)

        try:
            logging.error(f"Nikke-SignIn: {SignIn.json()}")
        except:
            if SignIn.text == "":
                logging.info("Nikke-SignIn: 簽到成功")

    def HoyolabCheckIn(self):

        StateParse = {
            "GenshInimpact": lambda retcode: (
                "簽到成功" if retcode == 0 else "已經簽到" if retcode == -5003 else "簽到失敗"
            ),
            "HonkaiStarRail": lambda retcode: (
                "簽到成功" if retcode == 0 else "已經簽到" if retcode == -5003 else "簽到失敗"
            ),
            # "ZenlessZoneZero": lambda retcode: "簽到成功" if retcode == 0 else "已經簽到", # -500012 "已經簽到", -500004 "操作頻繁"
        }

        async def Factory():
            works = [
                self.async_http_post(Name, Url, self.Headers, self.Cookies)
                for Name, Url in HoyolabAPI.items()
            ]

            for result in await asyncio.gather(*works):
                state = StateParse.get(result["Name"], lambda *args: result)(result["retcode"])
                logging.info(f"{result['Name']}: {state}")

        asyncio.run(Factory())

    def LeveCheckIn(self):

        StateParse = {
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

        async def Factory():
            works = [
                self.async_http_post(Name, Url, self.Headers, self.Cookies)
                for Name, Url in LeveCheckInAPI.items()
            ]

            for result in await asyncio.gather(*works):
                state = StateParse.get(result["Name"], lambda *args: result)(result["code"])
                logging.info(f"{result['Name']}: {state}")

        asyncio.run(Factory())

    def LeveState(self):
        ViewPoints = self.http_post(LeveStateAPI["ViewPoints"], self.Headers, self.Cookies)
        logging.info(f"Points: {ViewPoints.json()['data']['total_points']}")

        TaskStatus = self.http_post(LeveStateAPI["TaskStatus"], self.Headers, self.Cookies)
        for State in TaskStatus.json()["data"]["tasks"]:
            logging.info(
                f"任務: {State['task_name']} | 代號: {State['task_id']} | 完成: {State['reward_infos'][0]['is_completed']}"
            )
