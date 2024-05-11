# Client.py
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 3000))
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    client_socket.send(username.encode())
    client_socket.send(password.encode())
    
    response = client_socket.recv(1024).decode()
    print("Server response:", response)
    
    client_socket.close()

if __name__ == "__main__":
    main()
