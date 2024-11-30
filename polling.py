import asyncio

from aiogram import Dispatcher
from aiogram.types import BotCommand
from aiogram.utils.i18n import FSMI18nMiddleware, I18n
from motor.motor_asyncio import AsyncIOMotorClient

from bot import omi_telebot
from commands import Commands
from handlers.common import common_router
from handlers.settings import settings_router

from middlewares import UserMiddleware, QueryAnswerMiddleware
from mongo import db, MongoStorage
from settings import I18N_DOMAIN, LOCALES_DIR, MONGO_URL


async def set_commands():
    await omi_telebot.set_my_commands(
        [
            BotCommand(command=f'{Commands.START.command}', description=f'{Commands.START.name}'),
            BotCommand(command=f'{Commands.HELP.command}', description=f'{Commands.HELP.name}')
        ]
    )


async def main():
    storage = MongoStorage(AsyncIOMotorClient(MONGO_URL))

    store_dp = Dispatcher(storage=storage)
    # dp.message.setup(LoggingMiddleware())
    store_dp.message.middleware(UserMiddleware())
    store_dp.callback_query.middleware(QueryAnswerMiddleware())

    store_dp.callback_query.middleware(UserMiddleware())

    i18n = I18n(path=LOCALES_DIR, default_locale="en", domain=I18N_DOMAIN)

    store_dp.message.outer_middleware(FSMI18nMiddleware(i18n))
    store_dp.callback_query.outer_middleware(FSMI18nMiddleware(i18n))

    store_dp.include_router(common_router)
    store_dp.include_router(settings_router)

    if True:
        await set_commands()

    await asyncio.gather(store_dp.start_polling(omi_telebot))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())