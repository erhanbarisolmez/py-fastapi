from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket


app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
        
        
        
# WebSocket testi

@app.get("/r")
async def read_main():
    return {"msg": "Hello world"}


@app.websocket("ws2")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg" : "Hello WebSocket"})
    await websocket.close()
    
def test_read_main():
    client = TestClient(app)
    response = client.get("/r")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello world"}

def test_websocket():
    client = TestClient(app)
    with client.websocket_connect("/ws2") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "Hello WebSocket"}
    