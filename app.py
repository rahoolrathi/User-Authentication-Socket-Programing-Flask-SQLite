from flask import Flask
from models import db
from routes import setup_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chatapplicationdb_owner:o8OGWHwUcRj7@ep-jolly-heart-a1ajtkrl.ap-southeast-1.aws.neon.tech/chatapplicationdb?sslmode=require'

# Initialize database
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
