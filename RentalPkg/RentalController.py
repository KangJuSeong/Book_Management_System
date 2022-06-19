from RentalPkg.RentalService import RentalServie


class RentalController:
    
    def __init__(self, rid=None):
        self.rid = rid
        self.rs = RentalServie()
        
    def getRentalAttr(self):
        return self.rs.getRentalAttr(self.rid)
    
    def getRentalList(self):
        return self.rs.getRentalList()