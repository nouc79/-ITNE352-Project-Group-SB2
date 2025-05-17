# Multithreaded Flight arrival Client/Server Information System [ITNE352-Project-Group-SB2]


# Project Description
In this project, we made a client and server system that shows flight information. The server connects to an API to get flights from an airport, and it can handle many clients at the same time. The client can ask for arrived flights, delayed flights, or details of one flight. I also made a simple GUI using tkinter so the user can click buttons instead of typing in the terminal. 

**Semester :** Second Semester 2024-2025

- **Group Name:** SB2
- **Course Code:** ITNE352
- **Section:** 2
- **Student Name and ID:**
1. Fatima Ahmed Ahmed Mohsen - 202209641
2. haleema khamis ali - 202104099
3. 

## Table of Contents:
- Requirment
- How to Run the project
- The scripts
- Additional concept
- Acknowledgments
- Conclusion
- Resources

# Requirements :
1. **Install Python:** Make sure Python is installed on your computer. You can download it from here https://www.python.org/downloads/
2. **Install Required Python Libraries:** like requests for API calls or tkinter for GUI
3. **Download the Project Files**
4. **Run the Server then the Client:** Make sure the server is running before starting the client to avoid connection errors

# How to run our project:
First open two terminals, In the first terminal, we run the server by typing (python server.py),and then we enter the airport code.This connects to the API and saves the flight data. After starting the server we open a second terminal and run the terminal-based client by typing (python client.py). The client will ask you to enter your username then show a menu in the terminal with options to view arrived flights, delayed flights, get details of a particular flight by entering its code or quit.
Alternatively, you can run the GUI client by typing (client_gui.py). The client connects to the server and allows us to click buttons to get arrived flights, delayed flights, or check details of a specific flight by enter the flight code.

# The scripts :
Our project includes three Python scripts (server.py) to handle flight data and client connections, (client.py) for the basic terminal client, and (client_gui.py) which has a simple graphical interface using tkinter. Each client script (client.py or client_gui.py) can be used separately to connect to the server and interact with the system.
1. **server.py script:**
   
2. **client.py script:** The client script is a terminal-based program that allows users to connect to a server and request flight information It Python socket library to create a TCP socket for communication with the server. When the script starts it asks the user to enter a username and then establishes a connection to the server at the local host IP 127.0.0.1 on port 5050. After connecting it shows a simple menu with four options: view arrived flights, view delayed flights, check details of a specific flight using its IATA code or quit. Based on the user's choice the client sends the appropriate request to the server and displays the response it gets. The script keeps running in a loop until the user chooses to quit.
The main functionalities include handling user input, sending requests to the server, receiving and displaying server responses, and managing the socket connection.

3. **client_gui.py:** 

# Additional concept :

# Acknowledgments :
We would like to extend our heartfelt thanks to Dr. Mohammed Almeer for his immense contributions to our project. His valuable knowledge, guidance, and unwavering support have been instrumental in our success, and we are truly grateful for his generosity in sharing his expertise with us.

# Conclusion :
This project helped us to understand how client-server systems work using sockets in Python. We learned how to connect to an API, handle multiple clients with threads, and send and receive data between the client and server. also we added a GUI using tkinter to make the client easier to use. 

# Resources :
Since the GUI part was a new concept for me, I learned how to use tkinter by watching YouTube tutorials : https://www.youtube.com/watch?v=ibf5cx221hk
https://www.youtube.com/watch?v=TuLxsvK4svQ
