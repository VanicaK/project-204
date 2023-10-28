import socket
from threading import Thread

SERVER=None
IP_ADDRESS="127.0.0.1"
PORT=6000

CLIENTS=[]

def setup():
    print("\n\t\t\t\t\t ***Welcome to the game*** \n")

    global SERVER
    global IP_ADDRESS
    global PORT

    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    SERVER.listen(10)

    print('\t\t\t ***AWAITING INCOMING CONNECTIONS***\n')
