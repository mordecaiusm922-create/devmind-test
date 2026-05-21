def login(request):
    user = request.args.get("username")
    query = "SELECT * FROM users WHERE user=" + user
    db.execute(query)
