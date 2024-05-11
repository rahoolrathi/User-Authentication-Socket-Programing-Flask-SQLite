# app.py
from flask import Flask
from models import db
from routes import setup_routes
from database_operations import add_users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Initialize database
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

# Call function to add users
add_users(app)

setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
