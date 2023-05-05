def getID(ID_PATH) -> int:
    _id: int = 0
    with open(ID_PATH, 'r') as f:
        _id = int(f.readline())
    return _id

def upID(ID_PATH):
    _id: int = getID(ID_PATH)
    with open(ID_PATH, 'w') as f:
        f.write(str(_id+1)) 
        
def getManagerCode():
    with open("DBPkg/txt/ManagerCode.txt") as f:
        code = f.readline()
        return code