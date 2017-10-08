from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'bob', 'pass')
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}

'''
the username and password in the signature are gotten through the /auth
endpoint created by the jwt extension
this username and password will compare the username and passwords in the 
dictionary of users
if valid username is found and the password for that user matches the supplied password, then the user is found and returned
else, none
'''
def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

'''
called by jwt
if a user is found by authenticate with the username, then jwt will send a jw token
'''
def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)