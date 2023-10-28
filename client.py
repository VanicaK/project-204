import socket
from threading import Thread
from tkinter import *
import random

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT=6000
    IP_ADDRESS="127.0.0.1"
    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    thread=Thread(target=msgReceived)
    thread.start()

def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1

    nameWindow=Tk()
    nameWindow.title("login")
    nameWindow.geometry("800x600")

    screen_width=nameWindow.winfo_screenwidth()
    screen_height=nameWindow.winfo_screenheight()