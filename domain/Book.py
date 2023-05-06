class Book:
    def __init__(self, bid: int, name: str, author: str, isbn: int, isRental: bool, location: str):
        self.bid: int = bid
        self.name: str = name
        self.author: str = author
        self.isbn: int = isbn
        self.isRental: bool = isRental
        self.location: str = location

