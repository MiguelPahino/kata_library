class Library:

    def __init__(self):
        self.books = {}
        self.users = []
        self.loans = {}

    def borrow(self):
        pass

    def return_book(self):
        pass

    def available(self):
        pass


class Book:

    def __init__(self,isbn,title,total_copies):
        self.isbn = isbn
        self.title = title
        self.total_copies = total_copies
        self.available = True
        pass

    def borrow_copy(self):
        pass

    def return_copy(self):
        pass

    def is_available(self):
        pass


class User:

    def __init__(self,user_id):
        self.user_id = user_id
        active_loans = []

    def can_borrow(self):
        pass

    def add_loan(self):
        pass

    def remove_loan(self):
        pass

class Loan:

    def __init__(self):
        pass