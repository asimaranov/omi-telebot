from aiohttp import web
from aiohttp.web_request import BaseRequest

from api_server.models import Memory, RealtimePluginRequest

from bot import bot
from mongo import db


async def process_webhook(request: BaseRequest):
    request_json = await request.json()
    await db.requests.insert_one({'request': request_json, 'url': request.url})

    omi_id = request.match_info['omi_id']

    if request_json['structured']:
        memory = Memory.model_validate(request_json)
        await db.memories.insert_one(memory)

        link = await db.links.find_one({'omi_id': omi_id})
        telegram_id = link['telegram_id']

        await bot.send_message(telegram_id, f'{memory.structured.emoji} <b>{memory.structured.title}</b>\n{memory.structured.overview}')

        
    else:
        realtime = RealtimePluginRequest.model_validate(request_json)
        await db.realtime.insert_one(realtime)

    return web.json_response(
        {
            'ok': True,
        })
