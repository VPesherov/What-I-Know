import json
from aiohttp import web

from models import User, engine, init_orm, Session

app = web.Application()


#
# async def hello_world(request):
#     print(request.query)
#     print(await request.json())
#     print(request.headers)
#     return web.json_response({"hello": "world"})
#
# app.add_routes([
#     web.get('/hello/world', hello_world),
#     web.post('/hello/world', hello_world)
# ])

async def init_db(app: web.Application):
    print('START')
    await init_orm()
    yield
    print('FINISH')
    await engine.dispose()


app.cleanup_ctx.append(init_db)


def get_http_error(error_class, message):
    return error_class(
        text=json.dumps({'error': message}),
        content_type="application/json"
    )


async def get_user_by_id(session: Session, user_id: int):
    user = await session.get(User, user_id)
    if user is None:
        raise get_http_error(web.HTTPNotFound, message=f"User with {user_id} not found")
    return user


class UserView(web.View):

    @property
    def user_id(self):
        return self.request.match_info['user_id']

    async def get_user(self):
        async with Session() as session:
            return await get_user_by_id(session, self.user_id)

    async def get(self):
        user = self.user_id

    async def post(self):
        pass

    async def patch(self):
        pass

    async def delete(self):
        pass


app.add_routes([
    web.get('/user/{user_id:\d+}', UserView),
    web.patch('/user/{user_id:\d+}', UserView),
    web.delete('/user/{user_id:\d+}', UserView),
    web.post('/user', UserView),
])

web.run_app(app, port=8080)
