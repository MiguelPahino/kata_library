from library import Library, Book, User
import pytest

def test_user_can_borrow_available_book():
    library = Library()
    book = Book("123", "Clean Code", 2)
    user = User("u1")

    library.add_book(book)
    library.add_user(user)

    library.borrow("u1", "123")

    assert book.available_copies == 1

def test_cannot_borrow_if_no_copies_available():
    library = Library()
    book = Book("123", "DDD", 1)
    user = User("u1")

    library.add_book(book)
    library.add_user(user)

    library.borrow("u1", "123")

    with pytest.raises(Exception):
        library.borrow("u1", "123")
    
def test_user_cannot_have_more_than_three_loans():
    library = Library()
    user = User("u1")

    library.add_user(user)

    for i in range(3):
        book = Book(str(i), f"Book{i}", 1)
        library.add_book(book)
        library.borrow("u1", str(i))

    new_book = Book("999", "Extra", 1)
    library.add_book(new_book)

    with pytest.raises(Exception):
        library.borrow("u1", "999")

def test_return_book_increases_available_copies():
    library = Library()
    book = Book("123", "Refactoring", 1)
    user = User("u1")

    library.add_book(book)
    library.add_user(user)

    library.borrow("u1", "123")
    library.return_book("u1", "123")

    assert book.available_copies == 1

