import asyncio
import websockets
import pickle
from client_db_manager import create_db_table, insert_values

async def get_data():
    uri = "ws://localhost:3000"
    async with websockets.connect(uri) as websocket:
        await websocket.send("KeyorSomething")
        print("Key sent...")

        while True:
            create_db_table()
            data = await websocket.recv()
            data = pickle.loads(data)
            values = [*data.values()]
            print(*values)
            insert_values(*data.values())
            print('Data saved to db!')

asyncio.get_event_loop().run_until_complete(get_data())
asyncio.get_event_loop().run_forever()