class Library():
    def __init__(self):
        self.books = []
        self.users = []

    def add_books(self, book):
        self.books.append(book)

    def add_users(self, user):
        self.users.append(user)

    def find_book(self):
        pass

    def show_all_Books(books):
            print(books)    

    def issue_book_to_user(self):
        pass

    def return_book_from_user(self):
        pass



class User():
    def __init__(self, name, lastname, user_id):
        self.name = name
        self.lastname = lastname
        self.id = user_id

    def check_borrowed_books(self):
        print(f"Borrowed books: {self.borrowed_books}") 



class Book():
    def __init__(self, name, author, book_id, year, genre, is_available):
        self.name = name 
        self.author = author
        self.book_id = book_id
        self.year = year
        self.genre = genre
        self.is_available = is_available

    def show_info(self):
        print(f"{self.name} | {self.author} | {self.book_id} | {self.genre} | {self.year} | {self.is_available}")

    def toggle_status(self):
        pass

lib = Library()
book_1 = Book('Jack', 'Maxim', 1, 2025, 'fiction', True)
lib.add_books(book_1)

book_2 = Book('Luck', 'Vadim', 2, 2023, 'history', True)
lib.add_books(book_2)

book_3 = Book('Make', 'Vova', 3, 2024, 'Novel', True)
lib.add_books(book_3)

book_4 = Book('Leak', 'Vova', 4, 2021, 'history', True)
lib.add_books(book_4)

book_5 = Book('Goal', 'Vova', 5, 2017, 'Novel', True)
lib.add_books(book_5)

book_6 = Book('Cant hurt me', 'Vova', 6, 2015, 'self improvement', True)
lib.add_books(book_6)

book_7 = Book('The one', 'Vova', 7, 2020, 'Novel', True)
lib.add_books(book_7)

lib.show_all_Books()

user_1 = User('Maxim', 'Nakonechnuiy', 1)
lib.add_users(user_1)

user_2 = User('Vova', 'Nakonechnuiy', 2)
lib.add_users(user_2)

user_3 = User('Vadim', 'Nakonechnuiy', 3)
lib.add_users(user_3)



