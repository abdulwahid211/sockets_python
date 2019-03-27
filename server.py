import socket
import _thread
from message import Message
import pickle
import os
from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = "0.0.0.0"
    app.run(host=host, port=port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(100)
    list_of_clients = []
    print("Server Socket successfully created")
    m = Message("Server", "Welcome to the chatroom mate!")


def process(connect):
    connect.send(pickle.dumps(m))
    while True:
        try:
            data = connect.recv(2048)
            if data:
                user = pickle.loads(data)
                print("from connected  user: " + str(user._name))

                print("sending: " + str(user._message))
                broadcast(data, connect)

            else:
                print(str(user._name) + " has just left the chat")
                remove(connect)
                break

        except:
            continue


""" 

Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message 


"""


def broadcast(data, connect):
    for clients in list_of_clients:
        if clients != connect:
            try:
                clients.send(data)
            except:
                clients.close()

                # if the link is broken, we remove the client
                remove(clients)


"""The following function simply removes the object 
from the list that was created at the beginning of  
the program"""


def remove(connect):
    if connect in list_of_clients:
        list_of_clients.remove(connect)

@app.route("/")
def run():
    # a forever loop until client wants to exit
    while True:
        connection, addr = s.accept()

        print('Connected to :', addr[0], ':', addr[1])

        """Maintains a list of clients for ease of broadcasting 
           a message to all available people in the chatroom"""
        list_of_clients.append(connection)

        # Start a new thread and return its identifier
        _thread.start_new_thread(process, (connection,))

    s.close()

