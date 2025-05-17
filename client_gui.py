#Done by : Noora Sami 202203065
#(GUI)Graphical User Interface. 
# It part of the program that the user can see and interact with.
# Instead of using the terminal and typing commands, the user can use buttons, text boxes, and windows to use the program easily.
import tkinter as tk 
import socket

#I will connect to the server 
client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 5050))  
client_socket.sendall(b"Noora")  

#so here function will sends a message to the server for the arrives flight,
#then it will wait for server to reply, and when get the rplay will shows the result in the box
def get_arrived():
    client_socket.sendall(b"arrived") 
    response = client_socket.recv(4096).decode() 
    output_box.delete("1.0", tk.END)  
    output_box.insert(tk.END, response) 

#and for this function will also sends a message for delayed flight 
def get_delayed():
    client_socket.sendall(b"delayed") 
    response = client_socket.recv(4096).decode() 
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, response) 

#function to send details request with flight code
def get_details():
    flight_code = entry.get()
    message = f"details {flight_code}"
    client_socket.sendall(message.encode())
    response = client_socket.recv(4096).decode()
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, response)

root = tk.Tk()
#for root size
root.geometry("800x500")

#make title for this root
root.title("Flight Info-ITNE352")

#line to tell the user to enter the fligh code 
tk.Label(root, text="Enter Flight Code:").pack()
entry = tk.Entry(root)
entry.pack()

#buttons to send different types of requests
tk.Button(root, text="Show Arrived Flights", command=get_arrived).pack()
tk.Button(root, text="Show Delayed Flights", command=get_delayed).pack()
tk.Button(root, text="Get Flight Details", command=get_details).pack()

#box to display the server response
output_box = tk.Text(root, height=15, width=80)
output_box.pack()

# Start the GUI loop
root.mainloop()




