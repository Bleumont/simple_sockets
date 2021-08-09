import asyncio
from json.decoder import JSONDecoder
from json.encoder import JSONEncoder
import websockets
import json
from client_db_manager import create_db_table, insert_values

async def get_data():
    comprobardb = 'algo'
    if not comprobardb:
        create_db_table()

    uri = "ws://localhost:3000"
    async with websockets.connect(uri) as websocket:
        await websocket.send("KeyorSomething")
        print("Key sent...")
        while True:
            data = await websocket.recv()
            print((data))
            
            # insert_values(*item)
            # print('Data saved to db!')


	
asyncio.get_event_loop().run_until_complete(get_data())
asyncio.get_event_loop().run_forever()