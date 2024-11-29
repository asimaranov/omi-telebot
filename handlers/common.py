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

from mongo import db
from aiogram.utils.i18n import gettext as _

from utils import answer_message_or_query
from aiogram.utils.i18n import lazy_gettext as __

common_router = Router()


class LanguageCallback(CallbackData, prefix='lang'):
    lang: str

@common_router.message(Command(commands=['start']))
async def send_welcome(message: types.Message, state: FSMContext):
    await state.set_state(None)

    args = message.text.split(maxsplit=1)

    if len(args) > 1:
            await db.links.insert_one({'omi_id': args[1], 'telegram_id': message.chat.id})
            await db.users.update_one({'chat_id': message.chat.id}, {'$set': {'omi_id': args[1], 'telegram_id': message.chat.id}})

            await message.answer(f'Your account <b>{message.chat.id}</b> is linked to necklace {args[1]}')

    link = await db.links.find_one({'telegram_id': message.chat.id})
    connection_status = bool(link)

    connection_instructions = '''\
To connect necklace with bot, follow one of the following methods:

<b> Method 1 </b>
1. Open Omi app -> apps -> search <b>Omi Telebot</b>
1.1. Tap <b>Install App</b>
1.2. Tap <b>Setup Omi Telebot</b>

<b> Method 2 </b>
1. Open Omi app -> Settings -> Developer mode
1.1. Enable <b>Memory events</b>, <b>Realtime Transcript</b>, <b>Day summary</b>
1.2. Enter <b>Endpoint url</b> as https://omitelebot.com/webhook?uid={message.chat.id}
1.3. Click <b>Save</b> button
1.4. Open Omi app -> Profile, Copy <b>Your User Id</b>
1.5. Enter command /start Your User Id

'''

    result_text = _(
        f"""🤖 Welcome to the <b>Omi Telebot</b>

Here you can connect your necklace with telegram

Necklace connection status: {'✅ Connected' if connection_status else '⚠️ Not connected'}

{connection_instructions if not connection_status else ''}
""")

    await message.answer(result_text,
                         reply_markup=InlineKeyboardBuilder().add(Commands.GO_TO_ADMIN_SECTION.to_button()).as_markup(),
                         disable_web_page_preview=True
                         )

@common_router.message(Command(commands=[Commands.HELP.command]))
@common_router.callback_query(Commands.HELP.to_filter())
async def help(message_or_query: types.Message):
    text = _("""<b>🆘 Help</b>

✅ <b>Help</b>:  

✅ <b>Available commands:</b>
    /start — Launch bot
    /help — Help
    
✅ <b>Support:</b> a.simaranov@gmail.com
""")
    await answer_message_or_query(message_or_query)(
        text,
        reply_markup=InlineKeyboardBuilder().add(
            Commands.EXIT.to_button(payload=Commands.ADMIN_SECTION.callback_data)).as_markup(),
        disable_web_page_preview=True

    )
