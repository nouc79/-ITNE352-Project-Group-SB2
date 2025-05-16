import tkinter as tk 
import socket

root = tk.Tk()

# I will connect to the server 
client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 3522)) 
client_socket.sendall(b"Client")  

#for window size
root.geometry("800x500")

#make title for this window
root.title("Flight-ITNE352")




