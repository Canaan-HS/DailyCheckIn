from Modules import (
    os,
    Path,
    Json_Read,
    Json_Parse,
    CreateTask
)

current_path = Path(__file__).parent

def LevelinfiniteStart(Local=True):
    LogPath = current_path / "Log/LeveInfo.log"
    LevelinfiniteData = Json_Read(current_path / "Data/Levelinfinite.json") if Local else Json_Parse(os.getenv("LevelinfiniteData"))

    Task = CreateTask(
        LogPath,
        LevelinfiniteData['headers'],
        LevelinfiniteData['cookies']
    )

    Task.LeveCheckIn()
    Task.LeveState()

def DiscordStart(Local=True):
    LogPath = current_path / "Log/DiscordInfo.log"
    DiscordData = Json_Read(current_path / "Data/Discord.json") if Local else Json_Parse(os.getenv("DiscordData"))

    Task = CreateTask(
        LogPath,
        DiscordData['headers'],
        DiscordData['cookies'],
        DiscordData['data']
    )

    Task.DiscordSignIn()
    
def Hoyolab(Local=True):
    LogPath = current_path / "Log/HoyolabInfo.log"
    HoyolabData = Json_Read(current_path / "Data/Hoyolab.json") if Local else Json_Parse(os.getenv("HoyolabData"))

    Task = CreateTask(
        LogPath,
        HoyolabData['headers'],
        HoyolabData['cookies']
    )

    Task.HoyolabCheckIn()

if __name__ == "__main__":
    LevelinfiniteStart(False)
    DiscordStart(False)
    # Hoyolab()