# Done by: Fatima Ahmed Ahmed Mohsen - 202209641

import socket

Host= '127.0.0.1'
Port= 5050

#creating TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((Host, Port))

username = input("Enter your username: ")
client.send(username.encode())

#A looped menu with the following options:
while True:
    print("\nMenu:")
    print("Option 1: Arrived flights")
    print("Option 2: Delayed flights")
    print("Option 3: Details of a particular flight")
    print("Option 4: Quit")

    #Ask the user to choose an option
    option = input("Select an option from 1 to 4: ")

    #Option 1: Arrived flights
    if option == "1":
        client.send("arrived".encode())

    #Option 2: Delayed flights
    elif option == "2":
        client.send("delayed".encode())

    #Option 3: Details of a particular flight
    elif option == "3":
        while True:
            flight_code = input("Enter the flight IATA code:").strip()
            if flight_code:
                client.send(f"details {flight_code}".encode())
                break
            else:
                #If the user leave this option empty
                print("You must enter a flight code Please try again")
            continue
        

    #Option 4: Quit
    elif option == "4":
        client.send("quit".encode())
        break

    else:
        print("Invalid option Please try again")
        continue

    #Receive and display the server's response
    response = client.recv(8192).decode()
    print(response)

client.close()
