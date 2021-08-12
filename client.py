import asyncio
import websockets
import pickle
from client_db_manager import create_db_table, insert_values

async def get_data():
    uri = "ws://localhost:3000"
    async with websockets.connect(uri) as websocket:
        await websocket.send("KeyorSomething")
        print("Key sent...")
        # create_db_table()

        while True:
            data = await websocket.recv()
            data = pickle.loads(data)
            # print(pickle.loads(data))
            values = [*data]
            # print(*values)
            insert_values(*data)
            print('Data saved to db!')

asyncio.get_event_loop().run_until_complete(get_data())
asyncio.get_event_loop().run_forever()