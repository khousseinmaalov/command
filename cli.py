from tkinter import *
import threading
import socket


hote = "127.0.0.1"
port = 15555


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((hote, port))

print("Connection sur {}".format(port))


def debianeuf(event):

	olivier_de_carglasse = event.keysym
	if olivier_de_carglasse == "Down":
		kh_deb = "a"
		socket.send(kh_deb.encode())
		socket.send(kh_deb.encode())
		print(olivier_de_carglasse)
	if olivier_de_carglasse == "Up":
		kh_ma = "b"
		socket.send(kh_ma.encode())
		socket.send(kh_ma.encode())
		print(olivier_de_carglasse)
	if olivier_de_carglasse == "Right":
		kh_li = "c"
		socket.send(kh_li.encode())
		socket.send(kh_li.encode())
		print(olivier_de_carglasse)
	if olivier_de_carglasse == "Left":
		kh_kh = "d"
		socket.send(kh_kh.encode())
		socket.send(kh_kh.encode())
		print(olivier_de_carglasse)



def rien():

	fenetre = Tk()
	frame = Frame(fenetre, width=100, height=100)
	canvas = Canvas(fenetre, width=500, height=500)
	canvas.focus_set()
	threading.Thread(target=canvas.bind,args=("<Key>", debianeuf)).start()
	canvas.pack()

	frame.pack()

	fenetre.mainloop()
rien()
