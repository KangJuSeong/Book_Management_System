def getManagerCode():
    with open("DBPkg/txt/ManagerCode.txt") as f:
        code = f.readline()
        return code