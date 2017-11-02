from sanic import Sanic, response
from redis import StrictRedis
from config import REDIS_URL


app = Sanic(__name__)
redis_store = StrictRedis.from_url(REDIS_URL, decode_responses=True)


@app.route('/')
async def test(request):
    try:
        count = int(redis_store.get('simple_count'))
        count += 1
    except TypeError:
        count = 1
    redis_store.set('simple_count', count)
    response_data = {
        'message': 'Hello, world!',
        'count': count
    }
    return response.json(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)