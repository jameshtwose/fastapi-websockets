import websockets
import datetime
import asyncio



# send data to the server /ws endpoint
async def send_data():
    uri = "ws://localhost:8090/ws"
    async with websockets.connect(uri) as websocket:
        await websocket.send(f"Hello, world at {datetime.datetime.now()}")
        response = await websocket.recv()
        print(response)
        await asyncio.sleep(1)
        
if __name__ == "__main__":
    while True:
        asyncio.get_event_loop().run_until_complete(send_data())