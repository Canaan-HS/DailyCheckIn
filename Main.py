from Modules import os, Path, Json_Read, Json_Parse, CreateTask

current_path = Path(__file__).parent

"""
? 程式使用描述

Todo - 1. 根據要簽到的功能, 呼叫對應函數
Todo - 2. 如果是本地使用, 不需要傳遞任何參數
Todo - 3. 如果是環境變數使用, 可設置 EnvSource 參數 與 LogSave 參數

! 參數並無做檢查, 如果 EnvSource 不存在, 或格式不符合模板, 就直接壞掉
"""


def LevelinfiniteStart(EnvSource: str = None, LogSave: str = "Log/LeveInfo.log"):
    LogPath, LevelinfiniteData = (
        (current_path / LogSave, Json_Parse(os.getenv(EnvSource)))
        if isinstance(EnvSource, str)
        else (None, Json_Read(current_path / "Data/Levelinfinite.json"))
    )

    Task = CreateTask(LogPath, LevelinfiniteData["headers"], LevelinfiniteData["cookies"])

    Task.LeveCheckIn()
    Task.LeveState()


def DiscordStart(EnvSource: str = None, LogSave: str = "Log/DiscordInfo.log"):
    LogPath, DiscordData = (
        (current_path / LogSave, Json_Parse(os.getenv(EnvSource)))
        if isinstance(EnvSource, str)
        else (None, Json_Read(current_path / "Data/Discord.json"))
    )

    Task = CreateTask(LogPath, DiscordData["headers"], DiscordData["cookies"], DiscordData["data"])

    Task.DiscordSignIn()


def Hoyolab(EnvSource: str = None, LogSave: str = "Log/HoyolabInfo.log"):
    LogPath, HoyolabData = (
        (current_path / LogSave, Json_Parse(os.getenv(EnvSource)))
        if isinstance(EnvSource, str)
        else (None, Json_Read(current_path / "Data/Hoyolab.json"))
    )

    Task = CreateTask(LogPath, HoyolabData["headers"], HoyolabData["cookies"])

    Task.HoyolabCheckIn()


if __name__ == "__main__":
    # ? 本地端運行
    # Hoyolab()
    # DiscordStart()
    # LevelinfiniteStart()

    # ? GitHub Actions 運行
    # Hoyolab("HoyolabData")
    DiscordStart("DiscordData")
    # LevelinfiniteStart("LevelinfiniteData")
