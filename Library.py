class Library():
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def __str__(self):
        if self.books:
            books_str = "\n".join(f"{book.title} {book.author}" for book in self.books)
        else:
            books_str = "No items there"
        
        if self.users:
            users_str = "\n".join(f"{user.name} {user.lastname}" for user in self.users)
        else:
            users_str = "No items there"

        output = f"\n{books_str}\n\n{users_str}"
        return output 
    
    def show_all_books(self):
        books_str = "\n".join(f"{book.title} {book.author}" for book in self.books)
        return books_str

    def show_all_users(self):
        users_str = "\n".join(f"{user.name} {user.lastname}" for user in self.users)
        return users_str

    def show_borrowed_books(self):
        output_lines = []
        for i in self.users:
            borrowed_list = [book.title for book in i.borrowed_books]
            if borrowed_list:
                borrowed_str = ", ".join(borrowed_list)
                output_lines.append(f"{i.name} {i.lastname} borrowed: {borrowed_str}")
        return "\n".join(output_lines)

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def issue_book_to_user(self, user_id, book_id):
        user = self.get_user_by_id(user_id)
        book = self.get_book_by_id(book_id)

        if not user:
            return "User is not found"
        if not book:
            return "Book is not found"
        if not book.is_available:
            return f"Book {book} is not available"
        
        user.borrow_book(book)
        book.is_available = False
        return f"The Book {book} issued to {user}"
        
    def return_book_from_user(self, user_id, book_id):
        user = self.get_user_by_id(user_id)
        book = self.get_book_by_id(book_id)

        if not user or not book:
            return "User or Book not found"
        
        if book not in user.borrowed_books:
            return f"{user.name} does not have this book"

        user.return_book(book)
        book.is_available = True
        return f"The Book '{book.title}' is returned by {user.name}."
        


class User():
    def __init__(self, name, lastname, user_id):
        self.name = name
        self.lastname = lastname
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)   

    def __repr__(self):
        return f"{self.name!r} {self.lastname!r} {self.user_id}"
    
    def __str__(self):
        return f"{self.name} {self.lastname}  | id - {self.user_id}"
    
    def check_borrowed_books(self):
        if self.borrowed_books:
            borrowed_str = '\n'.join(f"{book.title} by {book.author} {book.book_id}" for book in self.borrowed_books)
        else:
            borrowed_str = "No borrowed books"
        return borrowed_str



class Book():
    def __init__(self, title, author, book_id, year, genre, is_available):
        self.title = title 
        self.author = author
        self.book_id = book_id
        self.year = year
        self.genre = genre
        self.is_available = is_available

    def __str__(self):
        return f"{self.title} | {self.author} | {self.book_id} | {self.genre} | {self.year} | {self.is_available}"
    
    def __repr__(self):
        return f"{self.title!r} {self.author!r} {self.year} {self.book_id} {self.genre} {self.is_available} "


lib = Library()
book_1 = Book('Jack', 'Maxim', 1, 2025, 'fiction', True)
lib.add_book(book_1)

book_2 = Book('Luck', 'Vadim', 2, 2023, 'history', True)
lib.add_book(book_2)

book_3 = Book('Make', 'Kola', 3, 2024, 'Novel', True)
lib.add_book(book_3)

book_4 = Book('Leak', 'Ola', 4, 2021, 'history', True)
lib.add_book(book_4)

book_5 = Book('Goal', 'Karina', 5, 2017, 'Novel', True)
lib.add_book(book_5)

book_6 = Book('Cant hurt me', 'David', 6, 2015, 'self improvement', True)
lib.add_book(book_6)

book_7 = Book('The one', 'John', 7, 2020, 'Novel', True)
lib.add_book(book_7)


user_1 = User('Maxim', 'Nakonechnuiy', 1)
lib.add_user(user_1)

user_2 = User('Vova', 'Nakonechnuiy', 2)
lib.add_user(user_2)

user_3 = User('Vadim', 'Nakonechnuiy', 3)
lib.add_user(user_3)


print(lib.issue_book_to_user(1, 6))
print()
print(lib.issue_book_to_user(1, 7))
print(lib.issue_book_to_user(1, 5))
print()
print(user_1.check_borrowed_books())
