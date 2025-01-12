class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"
book = Book("Мёртвые души", "Николай Гоголь", 1842)
print(book.info())