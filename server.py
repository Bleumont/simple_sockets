import asyncio
from asyncio.windows_events import NULL
from json import dumps
import websockets
import random 
import pickle
from server_db_manager import get_data_from_db

print('Waiting for clients...')

async def hello(websocket, path):
    print("Client connected.")
    try:
        async for message in websocket:
            if message == 'KeyorSomething':
                print('Password: ',message)
                print(f"Sending data to {websocket.remote_address[0]}")
                while websocket != NULL:
                    data = get_data_from_db('db.sqlite3')
     
                    for item in data:
                        await websocket.send(pickle.dumps(item))
                   
                    await asyncio.sleep(random.random() * 5)
    except websockets.exceptions.ConnectionClosed as msg:
        print(f"{websocket.remote_address[0]} disconnected, {msg}")


start_server = websockets.serve(hello, "localhost", 3000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()