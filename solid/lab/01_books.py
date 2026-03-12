class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, *books):
        self.books = list(books)

    def find_book(self, title):
        try:
            return [el for el in self.books if el.title == title][0]
        except IndexError:
            return "Book not found"

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)
