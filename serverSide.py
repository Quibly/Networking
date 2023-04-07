import socket
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = os.environ.get("serverIP")

# Reserve a port for your service
port = int(os.environ.get("serverPort"))

# Bind the socket to a public host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

# Wait for a client to connect
print("Waiting for a client to connect...")
client_socket, addr = server_socket.accept()

print(f"Connection from {addr} has been established!")

# Send a message to the client
menu = """\nHello! Thank you for connecting.

1. For a joke
2. For motivation
3. For the date
4. To close connection with server

Or just enter a custom message to tell the server admin.
(There's no guarantee that they'll get back to you.)

"""
client_socket.send(menu.encode())

# Loop for more messages
reply = ""
message = client_socket.recv(1024)
while message.decode() != '4':
    if message.decode() == '1':
        reply = "Life's like a bird. It's pretty cute until it poops on your head."
        client_socket.send(reply.encode())
        print("Sent reply 1")
    elif message.decode() == '2':
        reply = "'May your choices reflect your hopes, not your fears.' Nelson Mandela"
        client_socket.send(reply.encode())
        print("Sent reply 2")
    elif message.decode() == '3':
        today = date.today()
        reply = str(today)
        client_socket.send(reply.encode())
        print("Sent reply 3")
    else:
        print(f"Received message:    {message.decode()}")
        reply = input("\nPlease enter a response: ")
        client_socket.send(reply.encode())
        print('Sent custom response.')
    client_socket.send(menu.encode())
    message = client_socket.recv(1024)
    

# Close the connection
client_socket.close()
print("Connection closed.")