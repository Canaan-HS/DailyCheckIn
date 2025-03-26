# https://discord.com/channels/946719263866101821/1300742310186975232
DiscordAPI = {
    "SignIn": "https://discord.com/api/v9/interactions"
}

# ZenlessZoneZero 可能無法簽到
# https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481
# https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id=e202303301540311
# https://act.hoyolab.com/bbs/event/signin/zzz/e202406031448091.html?act_id=e202406031448091
HoyolabAPI = {
    "GenshInimpact": "https://sg-hk4e-api.hoyolab.com/event/sol/sign?act_id=e202102251931481",
    "HonkaiStarRail": "https://sg-public-api.hoyolab.com/event/luna/os/sign?act_id=e202303301540311",
    # "ZenlessZoneZero": "https://sg-public-api.hoyolab.com/event/luna/zzz/os/sign?act_id=e202406031448091"
}

# https://pass.levelinfinite.com/rewards?points=/points/
# https://pass.levelinfinite.com/rewards?points=/points/sign-in
LeveCheckInAPI = {
    "CheckIn": "https://api-pass.levelinfinite.com/api/rewards/proxy/lipass/Points/DailyCheckIn?task_id=15",
    "StageCheckIn": "https://api-pass.levelinfinite.com/api/rewards/proxy/lipass/Points/DailyStageCheckIn?task_id=58"
}

LeveStateAPI = {
    "ViewPoints": "https://api-pass.levelinfinite.com/api/rewards/proxy/lipass/Points/GetUserTotalPoints",
    "TaskStatus": "https://api-pass.levelinfinite.com/api/rewards/proxy/lipass/Points/GetTaskListWithStatusV2",
}