def process(request):
    user = request.args.get("username")
    cmd = "ls " + user
    os.system(cmd)
