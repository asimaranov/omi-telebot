from aiohttp import web
from aiohttp.web_request import BaseRequest

from api_server.models import Memory, RealtimePluginRequest

from bot import bot
from mongo import db


async def process_webhook(request: BaseRequest):
    request_json = await request.json()
    omi_id = request.rel_url.query['uid']

    if 'structured' in request_json:
        saved_request = await db.requests.find_one({'request.id': request_json['id']})
        print(saved_request)

        if saved_request:
            await db.doubled_request.insert_one({'request': request_json, 'omi_id': omi_id})
            return web.json_response(
                {
                    'ok': False,
                    'error': 'Duplicated request'
                }
            )

        memory = Memory.model_validate(request_json)
        await db.memories.insert_one({'memory': memory.model_dump(), 'omi_id': omi_id})

        link = await db.links.find_one({'omi_id': omi_id})
        telegram_id = link['telegram_id']
        if memory.structured.title:
            await bot.send_message(telegram_id, f'{memory.structured.emoji} <b>{memory.structured.title}</b>\n{memory.structured.overview}')
    else:
        realtime = RealtimePluginRequest.model_validate(request_json)
        await db.realtime.insert_one({'realtime': realtime.model_dump(), 'omi_id': omi_id})
    
    await db.requests.insert_one({'request': request_json, 'omi_id': omi_id})

    return web.json_response(
        {
            'ok': True,
        })
