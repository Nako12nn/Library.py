class Library():
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def find_book(self,book_id): 
        for book in self.books:
            if book.book_id == book_id:
               return book
        return None

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
        book = self.find_book(book_id)

        if not user:
            return "User is not found"
        if not book:
            return "Book is not found"
        if not book.is_available:
            return f"Book {book} is not available"
        
        user.borrowed_books.append(book)
        book.is_available = False
        return f"The Book {book} issued to {user}"
        
    def return_book_from_user(self, user_id, book_id):
        user = self.get_user_by_id(user_id)
        book = self.find_book(book_id)

        if not user and book:
            return "User or Book not found"
        
        if book not in user.borrowed_books:
            return f"{user.name} does not have this book"

        user.borrowed_books.remove(book)
        book.is_available = True
        return f"The Book '{book}' is returned by {user.name}."
        


class User():
    def __init__(self, name, lastname, user_id):
        self.name = name
        self.lastname = lastname
        self.user_id = user_id
        self.borrowed_books = []

    def check_borrowed_books(self):
       # print(self.borrowed_books)
       pass

    def __repr__(self):
        return f"{self.name!r} | {self.lastname!r} | {self.user_id}"
    
    def borrow_book(self):
        pass

    def return_book(self):
        pass    


class Book():
    def __init__(self, name, author, book_id, year, genre, is_available):
        self.name = name 
        self.author = author
        self.book_id = book_id
        self.year = year
        self.genre = genre
        self.is_available = is_available

    def __str__(self):
        return f"{self.name} | {self.author} | {self.book_id} | {self.genre} | {self.year} | {self.is_available}"
    
    def __repr__(self):
        return f"Book({self.name!r}, {self.author!r}, {self.year})"

    def toggle_status(self):
        self.is_available = not self.is_available
        return self.is_available

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

print(book_7,'\n',book_6)

print()

user_1 = User('Maxim', 'Nakonechnuiy', 1)
lib.add_user(user_1)

user_2 = User('Vova', 'Nakonechnuiy', 2)
lib.add_user(user_2)

user_3 = User('Vadim', 'Nakonechnuiy', 3)
lib.add_user(user_3)

for i in lib.users:
    print(i)

print()

print(lib.issue_book_to_user(1, 6))
print(user_1.borrowed_books)
print(lib.issue_book_to_user(1, 6))
print(lib.return_book_from_user(1, 6))
print(lib.issue_book_to_user(1, 6))

print(lib.issue_book_to_user(2, 7))
print(user_2.borrowed_books)


print(lib.issue_book_to_user(3, 5))
print(user_3.borrowed_books)

print(lib.find_book(5))
print(lib.find_book(7))
print(lib.find_book(6))

