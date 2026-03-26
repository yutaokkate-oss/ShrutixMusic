import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("32426469"))
API_HASH = getenv("6cc009055eb3c64d5b50d6cea35ebee8")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7981788706:AAEpCPckAoFdDRokiNP5dqB69N-YwmvxVXQ")


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://s72222980_db_user:43UUH5CnqQ19cnTW@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority")

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

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MOONIEEZ")
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
STRING1 = getenv("BAJdu6kAWWID1CsbRuIZDOckUNwWWqncTKbTf-8SDL2koa70qgrdBHdVhFkJag4yem2UKCAEQZaHJSzBGx6Wvsq9WDNdgRHOa-nlameaeJdyS_o5iIAcgOw-GS7E-sKGSnmCPW5dkOBVS0SBpzbAHuhFWwKiAJpeelb0ATsCwzrqJ_n7VYOyy_TC_JDsgCAos_I2XWGZsnW8-67ZO1MNx5cspd7j_ME-GDrcvpcP2z0pIeTe1XQToTFkeTj71Ne5livMKZFlu-yXC4hUenPtyny-a9EoeTi8_C4sipwfm35qrjxhs6bSzEUGIF7ZIPFoyw7NYy10UgsYRvAviX-wrtrnY2fORQAAAAIFzOn8AA", None)
STRING2 = getenv("STRING_SESSION2", None)
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
    "PING_IMG_URL", "https://files.catbox.moe/w9o758.jpg"
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
