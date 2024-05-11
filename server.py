# Server.py
import socket
import threading

def authenticate_user(username, password):
    # Dummy authentication function, replace with actual authentication logic
    return username == "admin" and password == "password"

def handle_client_connection(client_socket):
    username = client_socket.recv(1024).decode()
    password = client_socket.recv(1024).decode()
    
    if authenticate_user(username, password):
        client_socket.send(b"Authenticated")
        # Allow access to resources
    else:
        client_socket.send(b"Authentication failed")
        # Close connection or prompt for reauthentication
    
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(5)
    
    while True:
        client_socket, _ = server_socket.accept()
        client_handler = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
