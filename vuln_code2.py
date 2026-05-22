import pickle
import hashlib

def login(request):
    user = request.args.get("username")
    query = "SELECT * FROM users WHERE user=" + user
    db.execute(query)

def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()
