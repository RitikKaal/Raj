from PickUpLineMusic.core.bot import Tamanna
from PickUpLineMusic.core.dir import dirr
from PickUpLineMusic.core.git import git
from PickUpLineMusic.core.userbot import Userbot
from PickUpLineMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Tamanna()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
