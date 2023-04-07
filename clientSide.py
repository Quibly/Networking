import socket
from dotenv import load_dotenv
import os

load_dotenv()

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP address or hostname of the server
server_address = os.environ.get("serverIP")

# Port number that the server is listening on
server_port = int(os.environ.get("serverPort"))

# Connect to the server
client_socket.connect((server_address, server_port))

# Loop through messages from the server
selection = ''
while selection != '4':
    menu = client_socket.recv(1024).decode()
    selection = input(menu)
    if selection != '4':
        client_socket.send(selection.encode())
        message = client_socket.recv(1024).decode()
        print(f"Received message:   {message}")
    if selection == '4':
        client_socket.send(selection.encode())

# Close the connection
client_socket.close()