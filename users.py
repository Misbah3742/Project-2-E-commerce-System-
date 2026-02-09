import json

def register_user(username, email):
    user = {
        "username": username,
        "email": email
    }
    with open('users.json', 'a') as f:
        f.write(json.dumps(user) + '\n')
    return user