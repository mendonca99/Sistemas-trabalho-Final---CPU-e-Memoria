from flask import Flask, render_template
from flask_socketio import SocketIO
import redis
import json

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Conexão com Redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    print("Cliente conectado!")

@socketio.on("message")
def handle_message(data):
    if isinstance(data, str):  # Apenas faz json.loads() se for uma string
        data = json.loads(data)

    r.set("system_data", json.dumps(data))  # Guarda os dados no Redis
    socketio.emit("update", data)  # Envia os dados para o frontend

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
