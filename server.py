# Server.py
import socket
import threading
from models import db, User
from flask import current_app
from app import app

def authenticate_user(username, password):
    with app.app_context():
        user = User.query.filter_by(username=username, password=password).first()
        return user is not None

def handle_client_connection(client_socket):
    print("Client handler started")
    message = client_socket.recv(1024).decode()
    username, password = message.split(':')
    if authenticate_user(username, password):
        client_socket.send(b"Authenticated")
        print("Authentication successful")
        # Allow access to resources
    else:
        client_socket.send(b"Authentication failed")
        print("Authentication failed")
        # Close connection or prompt for reauthentication
    
    client_socket.close()
    print("Client handler ended")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 3000))
    server_socket.listen(5)
    
    while True:
        client_socket, _ = server_socket.accept()
        client_handler = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
