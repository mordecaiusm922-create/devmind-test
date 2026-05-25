import os
import pickle

def login(request):
    user = request.args.get("user")
    db.execute("SELECT * FROM users WHERE name = '" + user + "'")
    secret = "hardcoded_secret_key_12345"
    data = pickle.loads(request.data)
    return data
