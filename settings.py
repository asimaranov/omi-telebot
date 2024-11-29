from pathlib import Path
from environs import Env


env = Env()
env.read_env()

MONGO_DOMAIN = env.str('MONGO_DOMAIN')
BOT_TOKEN = env.str('BOT_TOKEN')

MONGO_URL = env.str('MONGO_URL')

I18N_DOMAIN = 'omi_telebot'
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'
