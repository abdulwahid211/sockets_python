# app.py
from flask import Flask, jsonify
app = Flask(__name__)
import socket
import _thread
from message import Message



@app.route('/')
def index():
    connection, addr = s.accept()
    print('Connected to :', addr[0], ':', addr[1])


if __name__ == '__main__':
    port = 8000
    host = "0.0.0.0"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    app.run()
    s.bind((host, port))
    s.listen(100)
    print("Server Socket successfully created")