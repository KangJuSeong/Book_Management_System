class User:

    def __init__(self, uid: int, name: str, address: str, phone: str, role: str, email: str):
        self.uid = uid
        self.name = name
        self.address = address
        self.phone = phone
        self.role = role
        self.email = email
    
    def __str__(self):
        return f"{self.uid}, {self.name}, {self.address}, {self.phone}, {self.role}, {self.email}"
