from Modules import (
    os,
    Path,
    Json_Read,
    Json_Parse,
    CreateTask
)

current_path = Path(__file__).parent

def LevelinfiniteStart(Local=True):
    LogPath, LevelinfiniteData = (
        (None, Json_Read(current_path / "Data/Levelinfinite.json"))
        if Local else (current_path / "Log/LeveInfo.log", Json_Parse(os.getenv("LevelinfiniteData")))
    )

    Task = CreateTask(
        LogPath,
        LevelinfiniteData['headers'],
        LevelinfiniteData['cookies']
    )

    Task.LeveCheckIn()
    Task.LeveState()

def DiscordStart(Local=True):
    LogPath, DiscordData = (
        (None, Json_Read(current_path / "Data/Discord.json"))
        if Local else (current_path / "Log/DiscordInfo.log", Json_Parse(os.getenv("DiscordData")))
    )

    Task = CreateTask(
        LogPath,
        DiscordData['headers'],
        DiscordData['cookies'],
        DiscordData['data']
    )

    Task.DiscordSignIn()

def Hoyolab(Local=True):
    LogPath, HoyolabData = (
        (None, Json_Read(current_path / "Data/Hoyolab.json"))
        if Local else (current_path / "Log/HoyolabInfo.log", Json_Parse(os.getenv("HoyolabData")))
    )

    Task = CreateTask(
        LogPath,
        HoyolabData['headers'],
        HoyolabData['cookies']
    )

    Task.HoyolabCheckIn()

if __name__ == "__main__":
    # Local 設置為 False 時, 通常無法在本地運行, 除非有額外設置 (主要用於 GitHub Actions)
    LevelinfiniteStart(False)
    DiscordStart(False)
    # Hoyolab()