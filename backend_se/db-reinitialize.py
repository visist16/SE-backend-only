from application import app
from application.models import *

db.drop_all()
db.create_all()


# Create 10 users
users_data = [
    {'username': 'user1', 'password': 'password1', 'email': 'user1@example.com', 'role': 1, 'discourse_id': 1001},
    {'username': 'user2', 'password': 'password2', 'email': 'user2@example.com', 'role': 1, 'discourse_id': 1002},
    {'username': 'user3', 'password': 'password3', 'email': 'user3@example.com', 'role': 2, 'discourse_id': 1003},
    {'username': 'user4', 'password': 'password4', 'email': 'user4@example.com', 'role': 2, 'discourse_id': 1004},
    {'username': 'user5', 'password': 'password5', 'email': 'user5@example.com', 'role': 3, 'discourse_id': 1005},
    {'username': 'user6', 'password': 'password6', 'email': 'user6@example.com', 'role': 3, 'discourse_id': 1006},
    {'username': 'user7', 'password': 'password7', 'email': 'user7@example.com', 'role': 4, 'discourse_id': 1007},
    {'username': 'user8', 'password': 'password8', 'email': 'user8@example.com', 'role': 4, 'discourse_id': 1008},
    {'username': 'user9', 'password': 'password9', 'email': 'user9@example.com', 'role': 1, 'discourse_id': 1009},
    {'username': 'user10', 'password': 'password10', 'email': 'user10@example.com', 'role': 1, 'discourse_id': 1010}
]

# Add users to the database
for user_data in users_data:
    user = User(**user_data)
    db.session.add(user)

# Commit the changes to the database
db.session.commit()
