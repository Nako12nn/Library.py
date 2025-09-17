import psycopg2

# Підключення до бази
conn = psycopg2.connect(
    dbname="library_db",
    user="maksym.com",     # тут вкажи свій юзер
    password="Ps-q-l34!!",   # пароль від Postgres
    host="localhost",
    port="5432"
)
conn = psycopg2.connect("postgresql://maksym.com:Ps-q-l34!!d@localhost:5432/library_db")
cur = conn.cursor()

class Library():
    def __init__(self):
        pass



class User():
    def __init__(self, name, lastname, id, borrowed_books):
        self.name = name
        self.lastname = lastname
        self.id = id
        self.borrowed_books = borrowed_books

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def check_borrowed_books(self):
        print(f"Borrowed books: {self.borrowed_books}") 




class Book():
    def __init__(self, name, author, id, year, genre, accessible):
        self.name = name 
        self.author = author
        self.id = id
        self.year = year
        self.genre = genre
        self.accessible = accessible

    def show_info(self):
        print(f"{self.name} | {self.author} | {self.id} | {self.genre} | {self.year} | {self.accessible}")

    def change_status(self):
        if self.accessible == True:
            self.accessible = False
        elif self.accessible == False:
            self.accessible = True
        if self.accessible:
            print(f"The book {self.name} is available")
        else: 
            print(f"The book {self.name} is unavailable")


    