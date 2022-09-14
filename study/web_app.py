import logging
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

import pytest

logging.basicConfig(level=logging.INFO)


def index(request):
    """
    :param request:
    :return:
    """
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init():
    """
    :param :
    :return:
    """
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app_runner = web.AppRunner(app)
    await app_runner.setup()
    srv = await loop.create_server(app_runner.server, '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()

if __name__ == '__main__':
    pytest.main()