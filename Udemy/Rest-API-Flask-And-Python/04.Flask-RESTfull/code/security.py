from werkzeug.security import safe_str_cmp
from user import User

# In memory table of registered users
users = [
    User(1, 'bob', 'asdf')
]

# Index on bob (username as key)
username_mapping = {u.username: u for u in users}

# ID as the key
userid_mapping = { u.id: u for u in users}

# Mapping means you don't have to iterate over these objects

# username_mapping['bob']
# userid_mapping[1]


def authenticate(username, password):
    user = username_mapping.get(username, None) # get the username, set to None by default if there is none
    if user and safe_str_cmp(user.password, password): # better way to do ==, dealing with ascii
        return user

# payload is the contents of JWT token
def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
