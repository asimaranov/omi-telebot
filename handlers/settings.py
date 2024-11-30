import re
from pathlib import Path

from aiogram import types, Router
from aiogram.filters import Command, StateFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, InputFile, BufferedInputFile, \
    FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from commands import Commands, CallbackMenuItem
from aiogram.types import CallbackQuery, Message
from mongo import db
from aiogram.utils.i18n import gettext as _

from utils import answer_message_or_query
from aiogram.utils.i18n import lazy_gettext as __

settings_router = Router()


class LanguageCallback(CallbackData, prefix='lang'):
    lang: str

@settings_router.message(Command(commands=[Commands.SETTINGS.command]))
@settings_router.callback_query(Commands.SETTINGS.to_filter())
async def settings(message_or_query: types.Message | types.CallbackQuery, state: FSMContext):
    pass

