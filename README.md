# fastapi-websockets
Quick demo of creating an API and using an API with websockets.

## Server
- Run the server with `python server.py`

## Client


## Extras
- `pip install -r requirements.txt`

#### Ubuntu
- `wget -qO /usr/local/bin/websocat https://github.com/vi/websocat/releases/latest/download/websocat.x86_64-unknown-linux-musl`
- `chmod a+x /usr/local/bin/websocat`
- `websocat ws://localhost:8090/ws`

#### MacOS
- `brew install websocat`
- `websocat ws://localhost:8090/ws`