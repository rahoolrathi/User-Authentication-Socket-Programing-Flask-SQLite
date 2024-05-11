# app/routes.py
from flask import render_template,request,redirect
import socket
def send_credentials_to_server(username, password):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        message = username + ':' + password
        client_socket.connect(('localhost', 3000))
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024).decode()
    return response


def setup_routes(app):
    @app.route('/homePage')
    def homepage():
        return render_template('homepage.htm')

    @app.route('/')
    def index():
        return render_template('login.htm')
    
    @app.route('/login', methods=['POST'])
    def login():
        print("hello")
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            print(username)
            print(password)
            response = send_credentials_to_server(username, password)
            if response == "Authenticated":
                 return redirect('/homePage')
            else:
                return render_template('login.htm', error_message="Incorrect credentials")

