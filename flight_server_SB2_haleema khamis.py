# flight_server_SB2.py
# ITNE352 Project - Server Script (Group SB2)
#done by: haleema khamis ali - 202104099


import socket
import threading
import json
import requests

# Server settings
HOST = '0.0.0.0'
PORT = 5050
API_KEY = 'bd4bd470311bb86a50764b3ec9b0f3e8'  
JSON_FILE = 'group_SB2.json'

# Getting data from aviationstack API
def get_flight_data(airport_code):
    url = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}&arr_icao={airport_code}&limit=100"
    res = requests.get(url)
    if res.status_code == 200:
        all_data = res.json()
        with open(JSON_FILE, 'w') as f:
            json.dump(all_data, f, indent=2)
        return all_data['data']
    else:
        print("API request failed.")
        return []

#  client requests
def handle_client(sock, addr, flight_data):
    try:
        name = sock.recv(1024).decode()
        print(f"Client connected: {name} from {addr}")

        while True:
            request = sock.recv(1024).decode().strip()
            if not request:
                break

            print(f"Request from {name}: {request}")
            if request == "arrived":
                result = get_arrived(flight_data)
            elif request == "delayed":
                result = get_delayed(flight_data)
            elif request.startswith("details"):
                parts = request.split(" ")
                if len(parts) > 1:
                    result = get_details(flight_data, parts[1])
                else:
                    result = "Missing flight code."
            else:
                result = "Invalid request."

            sock.send(result.encode())

    except:
        print(f"Error with client: {addr}")
    finally:
        print(f"Client disconnected: {name}")
        sock.close()

# Show arrived flights
def get_arrived(data):
    result = []
    for f in data:
        if f.get("flight_status") == "landed":
            info = f"{f['flight']['iata']}, {f['departure']['airport']}, {f['arrival']['actual']}, Terminal: {f['arrival'].get('terminal', 'N/A')}, Gate: {f['arrival'].get('gate', 'N/A')}"
            result.append(info)
    return "\n".join(result) or "No arrived flights."

# Show delayed flights
def get_delayed(data):
    result = []
    for f in data:
        delay = f.get("arrival", {}).get("delay", 0)
        if delay and delay > 0:
            info = f"{f['flight']['iata']}, {f['departure']['airport']}, Scheduled: {f['departure']['scheduled']}, ETA: {f['arrival']['estimated']}, Delay: {delay} min, Terminal: {f['arrival'].get('terminal', 'N/A')}, Gate: {f['arrival'].get('gate', 'N/A')}"
            result.append(info)
    return "\n".join(result) or "No delayed flights."

# Show details of one flight
def get_details(data, code):
    for f in data:
        if f['flight']['iata'].lower() == code.lower():
            return (
                f"Flight: {f['flight']['iata']}\n"
                f"Departure: {f['departure']['airport']}, Terminal: {f['departure'].get('terminal', 'N/A')}, Gate: {f['departure'].get('gate', 'N/A')}\n"
                f"Arrival: {f['arrival']['airport']}, Terminal: {f['arrival'].get('terminal', 'N/A')}, Gate: {f['arrival'].get('gate', 'N/A')}\n"
                f"Status: {f['flight_status']}\n"
                f"Scheduled Departure: {f['departure']['scheduled']}\n"
                f"Scheduled Arrival: {f['arrival']['scheduled']}"
            )
    return "Flight not found."

# Start server
def start_server(flight_data):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server running on {HOST}:{PORT}")

    while True:
        client_sock, client_addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_sock, client_addr, flight_data))
        thread.start()
        print(f"Connections: {threading.active_count() - 1}")

# Main
if __name__ == "__main__":
    code = input("Enter airport ICAO code: ")
    data = get_flight_data(code)
    if data:
        start_server(data)
