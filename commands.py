import typing
from dataclasses import dataclass

from aiogram.types import InlineKeyboardButton
from babel.support import LazyProxy
from aiogram.utils.i18n import lazy_gettext as __


@dataclass
class CallbackMenuItem:
    name: LazyProxy | str
    callback_data: str
    command: typing.Optional[str] = None

    def to_button(self, payload: str = ''):
        return InlineKeyboardButton(text=str(self.name), callback_data=payload or self.callback_data)

    def to_filter(self):
        return lambda c: c.data and c.data == self.callback_data


@dataclass
class CallbackMenuLink:
    name: LazyProxy | str
    url: str
    command: typing.Optional[str] = None

    def to_button(self, payload: str = '', format_: str = ''):
        return InlineKeyboardButton(text=str(self.name), url=(payload or self.url).format(format_))

    def to_filter(self):
        return None

class Commands:
    GO_TO_MAIN_MENU = CallbackMenuItem(__('🔥 Let\'s go'), 'go_to_menu')
    MAIN_MENU = CallbackMenuItem(__('Manage your necklace'), 'menu', command='menu')

    START = CallbackMenuItem('Manage your necklace', 'start', command='start')
    CONNECTION_INSTRUCTIONS = CallbackMenuItem(__('📜 Connection guide'), '', command='')
    SETTINGS = CallbackMenuItem('⚙️ Settings', 'settings', command='settings')

    SKIP_BOT = CallbackMenuItem(__('⏩ Skip'), 'skip_bot')

    HELP = CallbackMenuItem(('ℹ️ Help'), 'help', command='help')
    MANAGE_WALLET = CallbackMenuItem(__('⚙️ Wallet'), 'wallet', command='wallet')

    EXIT = CallbackMenuItem(__('«'), 'exit')
