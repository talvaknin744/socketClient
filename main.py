import socketio
import asyncio


loop = asyncio.get_event_loop()
sio = socketio.AsyncClient()


@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')

async def start_server():
    await sio.connect('http://localhost:8080')
    #await sio.emit('my message', {'data': 'foo!'})
    await sio.emit("test", {"data": "foo!"})
    await sio.wait()
       # explain sio.wait() here

if __name__ == '__main__':
    loop.run_until_complete(start_server())