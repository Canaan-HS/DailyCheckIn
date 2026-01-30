from Modules import os, Path, json_read, json_parse, CreateTask

current_path = Path(__file__).parent

"""
? 程式使用描述

Todo - 1. 根據要簽到的功能, 呼叫對應函數
Todo - 2. 如果是本地使用, 不需要傳遞任何參數
Todo - 3. 如果是環境變數使用, 可設置 env_source 參數 與 log_save_path 參數

! 參數並無做檢查, 如果 env_source 不存在, 或數據格式不符合模板, 就直接壞掉
"""


def levelinfinite_start(env_source: str = None, log_save_path: str = "Log/LeveInfo.log"):
    log_path, levelinfinite_data = (
        (current_path / log_save_path, json_parse(os.getenv(env_source)))
        if isinstance(env_source, str)
        else (None, json_read(current_path / "Data/Levelinfinite.json"))
    )

    task = CreateTask(log_path, cookies=levelinfinite_data["cookies"])

    task.leve_checkIn()
    task.leve_state()


def discord_start(env_source: str = None, log_save_path: str = "Log/DiscordInfo.log"):
    log_path, discord_data = (
        (current_path / log_save_path, json_parse(os.getenv(env_source)))
        if isinstance(env_source, str)
        else (None, json_read(current_path / "Data/Discord.json"))
    )

    task = CreateTask(log_path, headers=discord_data["headers"], cookies=discord_data["cookies"])

    task.nikke_discord_signIn(discord_data["signin-data"])
    # task.nikke_input_cdKey(discord_data["cdkey-data"])


def hoyolab(env_source: str = None, log_save_path: str = "Log/HoyolabInfo.log"):
    log_path, hoyolab_data = (
        (current_path / log_save_path, json_parse(os.getenv(env_source)))
        if isinstance(env_source, str)
        else (None, json_read(current_path / "Data/Hoyolab.json"))
    )

    task = CreateTask(log_path, cookies=hoyolab_data["cookies"])

    task.hoyolab_checkIn()


if __name__ == "__main__":
    # ? 本地端運行
    # hoyolab()
    # discord_start()
    # levelinfinite_start()

    # ? GitHub Actions 運行
    # hoyolab("HoyolabData")
    discord_start("DiscordData")
    # levelinfinite_start("LevelinfiniteData")
