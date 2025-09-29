class Library():
    def __init__(self):
        self._books = []
        self.users = []

    def add_book(self, book):
        self._books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def find_book(self):
        pass 

    def issue_book_to_user(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id
        user = None 
        for i in self.users, range(1, 3):
            if i == user_id:
                for j in self._books:
                    if j == book_id:
                        print("I found it!")
            else:
                print("I didnt find it..")    

    def return_book_from_user(self):
        pass



class User():
    def __init__(self, name, lastname, user_id, borrowed_books):
        self.name = name
        self.lastname = lastname
        self.user_id = user_id
        self.borrowed_books = []

    def check_borrowed_books(self):
        print(f"Borrowed books: {self.borrowed_books}")

    def __repr__(self):
        return f"{self.name!r} | {self.lastname!r} | {self.user_id}"
    
    def borrow_book(self):
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
        return "available" if self.is_available else "unavailable"

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

user_1 = User('Maxim', 'Nakonechnuiy', 1, "sth")
lib.add_user(user_1)

user_2 = User('Vova', 'Nakonechnuiy', 2, "sth")
lib.add_user(user_2)

user_3 = User('Vadim', 'Nakonechnuiy', 3, "sth")
lib.add_user(user_3)

for i in lib.users:
    print(i)

print()
print("All books:")
for i,book in enumerate(lib._books, start=1):
    print(i, book)

book_5.toggle_status()

print()

for s in user_1.borrowed_books:
    print(s)
print()
lib.issue_book_to_user(3, 6)

