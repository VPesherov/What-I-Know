import asyncio
import aiohttp
import datetime
from more_itertools import chunked

from models import init_db, Session, SwapiPeople

MAX_CHUNK = 5


async def get_person(person_id, session):
    http_response = await session.get(f"https://swapi.py4e.com/api/people/{person_id}/")
    json_data = await http_response.json()
    return json_data


async def insert_records(records):
    records = [SwapiPeople(json=record) for record in records]
    async with Session() as session:
        session.add_all(records)
        await session.commit()


async def main():
    await init_db()
    print('start')
    # открыли сессию
    session = aiohttp.ClientSession()

    for people_id_chunk in chunked(range(1, 20), MAX_CHUNK):
        coros = [get_person(person_id, session) for person_id in people_id_chunk]
        result = await asyncio.gather(*coros)
        # task - не блокирует дальнейшее выполнения кода
        task = asyncio.create_task(insert_records(result))
        print(result)
    await session.close()
    all_tasks_set = asyncio.all_tasks() - {asyncio.current_task()}
    await asyncio.gather(*all_tasks_set)

start = datetime.datetime.now()
asyncio.run(main())
print(datetime.datetime.now() - start)
