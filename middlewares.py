import asyncio

from aiogram.types import Message, CallbackQuery
from typing import Any, Callable, Dict, Awaitable

from aiogram import types, BaseMiddleware
from pymongo import ReturnDocument

from mongo import db
import secrets
import traceback

class UserMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        super().__init__()

    async def __call__(
            self,
            handler: Callable[[Message or CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message or CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        chat_id = event.chat.id if isinstance(event, Message) else event.message.chat.id if event.message else int(event.chat_instance)
        user: types.User = event.from_user

        db_user = await db.users.find_one_and_update(
            {"chat_id": chat_id},
            {"$setOnInsert": {
            },
                "$set": {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'username': user.username,
                },

            },
            upsert=True,
            return_document=ReturnDocument.AFTER)

        data['omi_id'] = db_user.get('omi_id')

        return await handler(event, data)


class QueryAnswerMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:

        result = await handler(event, data)
        await event.answer()
        return result
