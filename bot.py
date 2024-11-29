import typing
from aiogram import Bot
from aiogram.utils.i18n import lazy_gettext
from babel.support import LazyProxy
from aiogram.client.default import DefaultBotProperties
from settings import BOT_TOKEN
import logging

logging.basicConfig(level=logging.DEBUG)


def __(*args: typing.Any, **kwargs: typing.Any) -> LazyProxy:
    return lazy_gettext(*args, **kwargs, enable_cache=False)


omi_telebot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

bot = omi_telebot

