import psutil
import time
import socketio

sio = socketio.Client()

SERVER_URL = "http://127.0.0.1:5000"

try:
    sio.connect(SERVER_URL)
    print("Conectado ao servidor!")
except socketio.exceptions.ConnectionError as e:
    print(f"Erro de conexão: {e}")

while True:
    data = {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent
    }
    sio.send(data)  # Envia os dados
    print(f"Enviado: {data}")
    time.sleep(1)
