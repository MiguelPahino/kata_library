class Library:

    def __init__(self):
        self.books = {}
        self.users = {}
        self.loans = []

    def borrow(self,user_id, book_isbn):
        book = self.books[book_isbn]
        user = self.users[user_id]
        
        if not self.available(book):
            raise Exception("No hay copias disponibles en este momento.")
        
        if not user.can_borrow():
            raise Exception("Ya tienes tres libros.")
        
        book.available_copies -= 1
        user.add_loan(book_isbn)
        self.loans.append(Loan(user_id,book_isbn))
            
    def return_book(self,user_id,book_isbn):
        loan = self.find_loan(user_id,book_isbn)
        self.loans.remove(loan)
        self.users[user_id].active_loans.remove(loan)
        
    def find_loan(self,user_id,book_isbn):
        index = 0
        while index < len(self.loans):
            if self.loans[index].user_id == user_id and self.loans[index].book_isbn == book_isbn:
                return self.loans[index]
            index += 1
        raise Exception("No se encuentra el Loan")

    def available(self,book):
        return book.is_available()

    def add_book(self,book):
        if book.isbn in self.books:
            self.books[book.isbn].total_copies += book.total_copies
            self.books[book.isbn].available_copies += book.total_copies

        self.books[book.isbn] = book

    def add_user(self, user):
        self.users[user.user_id] = user


class Book:

    def __init__(self,isbn,title,total_copies):
        self.isbn = isbn
        self.title = title
        self.total_copies = total_copies
        self.available_copies = total_copies

    def is_available(self):
        return  self.available_copies > 0

    def borrow_copy(self):
        if self.is_available():
            self.available_copies -= 1

    def return_copy(self):
        self.available_copies += 1


class User:

    def __init__(self,user_id):
        self.user_id = user_id
        self.active_loans = []

    def can_borrow(self):
        return len(self.active_loans) < 4

    def add_loan(self,book_isbn):
        self.active_loans.append(Loan(self.user_id,book_isbn))

    def remove_loan(self,loan):
        self.active_loans.remove(loan)

class Loan:

    def __init__(self,user_id,book_isbn):
        self.user_id = user_id
        self.book_isbn = book_isbn