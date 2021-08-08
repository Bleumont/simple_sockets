import asyncio
import websockets
from client_db_manager import create_db_table, insert_values

async def get_data():
    comprobardb = 'algo'
    if not comprobardb:
        create_db_table()

    uri = "ws://localhost:3000"
    async with websockets.connect(uri) as websocket:
        await websocket.send("KeyorSomething")
        print("Sending request...")
        while True:
            data = await websocket.recv()
            print(f"{data}")
            insert_values(data)
            print('Data saved to db!')

	

asyncio.get_event_loop().run_until_complete(get_data())
# asyncio.get_event_loop().run_forever()