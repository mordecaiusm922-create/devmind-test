import os

def login(request):
    user = request.args.get("username")
    # SQL injection
    query = "SELECT * FROM users WHERE user = '" + user + "'"
    db.execute(query)

def run_command(request):
    cmd = request.args.get("cmd")
    # Command injection
    os.system(cmd)
