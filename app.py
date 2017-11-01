from sanic import Sanic, response
# import aioredis

from config import REDIS_URL


app = Sanic(__name__)


@app.route('/')
async def test(request):
    async with request.app.redis_pool.get() as redis:
        count = await redis.get('simple_count')
        try:
            count += 1
        except SyntaxError:
            count = 1
        await redis.set('simple_count', count)

    response_data = {
        'message': 'Hello, world!',
        'count': count
    }
    return response.json(response_data)


@app.listener('before_server_start')
async def before_server_start(app, loop):
    # app.redis_pool = await aioredis.create_pool(
    #     REDIS_URL,
    #     minsize=5,
    #     maxsize=10
    # )


@app.listener('after_server_stop')
async def after_server_stop(app, loop):
    app.redis_pool.close()
    await app.redis_pool.wait_closed()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)