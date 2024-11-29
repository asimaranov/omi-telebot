import asyncio
import os
import uuid
from datetime import datetime
from urllib.parse import urlencode

from PIL import Image
import aiogram
from aiogram import Bot
from aiohttp import web
from aiohttp.web_request import BaseRequest
from bson import ObjectId
from eth_account import Account
from eth_account.signers.local import LocalAccount

from api_server.models import Memory, RealtimePluginRequest
from bot import bot

from mongo import db


async def process_webhook(request: BaseRequest):
    request_json = await request.json()

    if request_json['structured']:
        memory = Memory.model_validate(request_json)
        await db.memories.insert_one(memory)

    else:
        realtime = RealtimePluginRequest.model_validate(request_json)
        await db.realtime.insert_one(realtime)

    return web.json_response(
        {
            'ok': True,
        })
