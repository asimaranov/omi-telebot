from aiohttp import web
from aiohttp.abc import BaseRequest

from api_server.methods import process_webhook

routes = web.RouteTableDef()

@routes.get(r'/webhook')
async def webhook_post(request: BaseRequest):
    """
        ---
        description: Approves webhook info.
        tags:
        - Webhook handler
        produces:
        - application/json
        parameters:
        responses:
            responses:
            "200":
                schema:
                    type: object
                    properties:
                      ok:
                        type: boolean
                        description: Is request succeeded.
                        default: true
        """
    return web.json_response({
        "ok": True
    })


@routes.post(r'/webhook')
async def webhook_post(request: BaseRequest):
    """
        ---
        description: Processes webhook call
        tags:
        - Webhook handler
        produces:
        - application/json
        parameters:
        responses:
            responses:
            "200":
                schema:
                    type: object
                    properties:
                      ok:
                        type: boolean
                        description: Is request succeeded.
                        default: true
            "500":
                description: Returns information about error
                schema:
                    type: object
                    properties:
                      ok:
                        type: boolean
                        description: Is request succeeded.
                        default: false
                      error:
                        type: string
                        description: Error message.
                        default: "Something went wrong"
        """
    return await process_webhook(request)


@routes.get(r'/setup')
async def setup_request(request: BaseRequest):
    """
        ---
        description: Used to setup bot
        tags:
        - Webhook handler
        produces:
        - application/json
        parameters:
        responses:
            responses:
            "200":
                schema:
                    type: object
                    properties:
                      ok:
                        type: boolean
                        description: Is request succeeded.
                        default: true
        """
    return web.json_response({
        "ok": True,
        "url": request.url.query_string
    })