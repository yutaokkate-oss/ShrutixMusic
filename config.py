import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("32426469"))
API_HASH = getenv("6cc009055eb3c64d5b50d6cea35ebee8")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7981788706:AAHDyVqSAijbXaRi3q98mQj_ANRS0xhkNDA")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002731144240"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 8353047575))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/yutaokkate-oss/ShrutixMusic.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ABOUTxYUTA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+NQGCtLEJJEo3OWY1")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQJdu6kAoX7BWrAj4fppBsqLWTkYriNmpu7eEl7SVaRG6K_b9YLPwI3RLTqmOL7zdrfJYbyy1vf3nRl_MZ5alwKQ12eKIN26v8bdFtR_iZGhwLLoSNSCwI0ny-wWge2FEc3DOEJ1kGgux0EwqdSQ6GnYeydPuIJ0cPRvMxpscGPnDcvFLbCZRE34VZlTAMk3F3NLHzvg2MqtlQ5dGIfZYMceIwfxtZF8cWj3iJO99RroAXsqtVKURwi9LUHiWX2iRMPKU-psn5Q5Lks3Nkc9I-7grWgP0u2UNZa6OTFjJ7wCATYqLN3944Ewjk_qptVt6RGdTUVRZ8avhWJYOzsn6poDt7pTEAAAAAGZ_ZuoAA", None)
STRING2 = getenv("BAJdu6kAmK6JNAoTzvvcY_U0j7kO6n7ZfZ0fnXz-Kh7Tq6bikUyu5Y06NTPMOwp_VtuWJYvaS4uNmFiDiKa38PCKFi9NpS3I15EYUucFYydXl-AoW_V_jEYGTYzpwrRXkh7plbfq9U-5wECeg30fI_y7MKHVV8bMBHdrCKKNS8mJAo1haMDef2V9KO6cxUDYFDHOSgoxNPFh_mBO5lBjPps-v6nb1gCbBZsi8WVDZYitoaBKQ4HMVWBiJzPXucn14lHxw-0576fPmYD9Brtz_6-U8_gru26wJkC_1g0i6n9J1dGPLcOMxVHrMC3rqHI0ImnmYd4URrIWfPkM1CZLH96Vzrl0wAAAAAIEB3suAA", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/66dl4g.mp4"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/66dl4g.mp4"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/2d2v8w.mp4"
STATS_IMG_URL = "https://files.catbox.moe/t229wh.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/i1xlds.mp4"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/i1xlds.mp4"
STREAM_IMG_URL = "https://files.catbox.moe/hcgw94.mp4"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/hcgw94.mp4"
YOUTUBE_IMG_URL = "https://files.catbox.moe/hcgw94.mp4"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/fme4nt.mp4"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/fme4nt.mp4"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/fme4nt.mp4"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
