import socket
import select
import sys
from message import Message
import pickle

host = '127.0.0.1'

port = 12345

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((host, port))

_name = str(sys.argv[1])
m = Message(_name, "")

while True:
    sockets_list = [sys.stdin, mySocket]

    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

    """ 
         There are two possible input situations. Either the
   #     user wants to give  manual input to send to other people,
   #     or the server is sending a message  to be printed on the
   #     screen. Select returns from sockets_list, the stream that
   #     is reader for input. So for example, if the server wants
   #     to send a message, then the if condition will hold true
   #     below.If the user wants to send a message, the else
   #     condition will evaluate as true
   
   """

    for socks in read_sockets:

        if socks == mySocket:
            data = socks.recv(2048)
            tm = pickle.loads(data)
            print(str(tm._name)+": " + str(tm._message))
        else:
            """
            < _io.TextIOWrapper
            name = '<stdin>'
            mode = 'r'
            encoding = 'UTF-8' >

            """
            message = input()
            m.updateMessage(message)
            mySocket.send(pickle.dumps(m))

mySocket.close()
