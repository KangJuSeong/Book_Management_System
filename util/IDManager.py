def getManagerCode():
    with open("./ManagerCode.txt") as f:
        code = f.readline()
        return code