from Modules import (
    Path,
    Json_Read,
    CreateTask
)

current_path = Path(__file__).parent

def LevelinfiniteStart():
    LevelinfiniteData = Json_Read(current_path / "Data/Levelinfinite.json")

    Task = CreateTask(
        LevelinfiniteData["headers"],
        LevelinfiniteData["cookies"]
    )

    Task.LeveCheckIn()
    Task.LeveState()

def DiscordStart():
    DiscordData = Json_Read(current_path / "Data/Discord.json")

    Task = CreateTask(
        DiscordData["headers"],
        DiscordData["cookies"],
        DiscordData["data"]
    )

    Task.DiscordSignIn()

LevelinfiniteStart()
DiscordStart()