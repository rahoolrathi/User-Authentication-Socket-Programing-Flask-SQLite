# database_operations.py
from models import db, User
def add_users(app):
    with  app.app_context():
        if not User.query.all():
            users_data = [
                ('user1', 'password1'),
                ('user2', 'password2'),
                ('user3', 'password3'),
                ('user4', 'password4'),
                ('user5', 'password5'),
                ('user6', 'password6'),
                ('user7', 'password7'),
                ('user8', 'password8'),
                ('user9', 'password9'),
                ('user10', 'password10')
            ]
            for username, password in users_data:
                new_user = User(username=username, password=password)
                db.session.add(new_user)
            db.session.commit()
