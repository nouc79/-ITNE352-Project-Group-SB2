# Multithreaded Flight arrival Client/Server Information System [ITNE352-Project-Group-SB2]


# Project Description
In this project, we made a client and server system that shows flight information. The server connects to an API to get flights from an airport, and it can handle many clients at the same time. The client can ask for arrived flights, delayed flights, or details of one flight. I also made a simple GUI using tkinter so the user can click buttons instead of typing in the terminal. 

**Semester :** Second Semester 2025-2026

- **Group Name:** SB2
- **Course Code:** ITNE352
- **Section:** 2
- **Student Name and ID:**
1. Fatima Ahmed Ahmed MOhsen - 202209641
2. haleema khamis ali - 202104099
3. 

## Table of Contents:
- Requirment
- How to Run
- The scripts
- Additional concept
- Acknowledgments
- Conclusion.

# Requirements :

# How to run our project:
we first open two terminals,In the first terminal, we run the server by typing (python server.py),and then we enter the airport code.This connects to the API and saves the flight data. After that, we open a second terminal and run the client by typing python (client_gui.py). The client connects to the server and allows us to click buttons to get arrived flights, delayed flights, or check details of a specific flight by enter the flight code.

# The scripts :
Our project includes three Python scripts (server.py) to handle flight data and client connections, (client.py) for the basic terminal client, and (client_gui.py) which has a simple graphical interface using tkinter. Each script works together to make the system easy to use and understand.

# Additional concept :

# Acknowledgments :
We would like to extend our heartfelt thanks to Dr. Mohammed Almeer for his immense contributions to our project. His valuable knowledge, guidance, and unwavering support have been instrumental in our success, and we are truly grateful for his generosity in sharing his expertise with us.

# Conclusion :
This project helped us to understand how client-server systems work using sockets in Python. We learned how to connect to an API, handle multiple clients with threads, and send and receive data between the client and server. also we added a GUI using tkinter to make the client easier to use. 

# Resources :
Since the GUI part was a new concept for me, I learned how to use tkinter by watching YouTube tutorials : https://www.youtube.com/watch?v=ibf5cx221hk
https://www.youtube.com/watch?v=TuLxsvK4svQ
