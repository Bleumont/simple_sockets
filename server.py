import asyncio
from asyncio.windows_events import NULL
import websockets
import random 
from server_db_manager import get_data_from_db

async def hello(websocket, path):
    print("Client connected.")
    try:
        async for message in websocket:
            if message == 'KeyorSomething':
                print("Sending data!")
                data = get_data_from_db('db.sqlite3') 
                await websocket.send("Connected... wait for data...")
                await asyncio.sleep(random.random() * 5)
                while websocket != NULL:
                    await websocket.send(data)
                    await asyncio.sleep(random.random() * 5)
    except websockets.exceptions.ConnectionClosed as msg:
        print(f"Client disconnected, {msg}")


start_server = websockets.serve(hello, "localhost", 3000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()