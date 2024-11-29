import asyncio
import logging

import aiohttp_cors
from aiohttp import web
from aiohttp_swagger import *

from api_server.endpoints import routes

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app = web.Application()

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    app.add_routes(routes)

    for resource in app.router.routes():
        cors.add(resource)

    setup_swagger(app, swagger_url='/doc', ui_version=2)

    app["SWAGGER_TEMPLATE_CONTENT"] = app["SWAGGER_TEMPLATE_CONTENT"].replace('docExpansion: "none"', 'docExpansion: "list"')

    web.run_app(app, port=25013, loop=asyncio.get_event_loop())


