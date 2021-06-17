import socket
import time
import threading
from tkinter import *

root = Tk()

root.geometry("300*500")
root.config(bg="white")


def func():
    t = threading.Thread(target=recv)
    t.start()


def recv():
    listensocket = socket.socket()
    port = 3050
    max_connection = 99
    ip = socket.gethostname()
    print(ip)

    listensocket.bind(("", port))
    listensocket.listen(max_connection)
    (client_socket, address) = listensocket.accept()

    while True:
        sendermessage = client_socket.recv(1024).decode()
        if not sendermessage == "":
            time.sleep(5)
            lstbox.insert(0, "Client: " + sendermessage)


x = 0


def sendmsg():
    global x
    if x == 0:
        s = socket.socket()
        hostname = ""
        port = 4050
        s.connect((hostname, port))
        msg = messagebox.get()
        lstbox.insert(0, "you:" + msg)
        s.send(msg.encode())
        x = x + 1
    else:
        s = socket.socket()
        msg = messagebox.get()
        lstbox.insert(0, "you:" + msg)
        s.send(msg.encode())


def threadsendmessage():
    th = threading.Thread(target=sendmsg)
    th.start()


startimage = PhotoImage(file="start.png")
buttons = Button(root, image=startimage, command=func, borderwidth=0)
buttons.place(x=90, y=10)

message = StringVar()
messagebox = Entry(root, textvariable=message, font=("calibre", 10, "normal"), border=2, width=3)
messagebox.place(x=10, y=444)

sendmessgae = PhotoImage(file="sendmessage.png")
sendmsgg = Button(root, image=sendmessgae, command=threadsendmessage, borderwidth=0)
sendmsgg.place(x=260, y=440)

lstbox = Listbox(root, width=43, height=20)
lstbox.place(x=15, y=80)

root.mainloop()
