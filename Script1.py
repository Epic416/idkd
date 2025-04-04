import sqlite3
import random

LibaryDB = sqlite3.connect("Libary.db")
cursor = LibaryDB.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS books ("
               "book_id INTEGER,"
               "title TEXT,"
               "author TEXT,"
               "year INTEGER,"
               "available INTEGER DEFAULT 1)")

cursor.execute("CREATE TABLE IF NOT EXISTS readers ("
               "reader_id INTEGER,"
               "name TEXT,"
               "phone INTEGER,"
               "book_id INTEGER)")

def add_book(title, author, year):
    LibaryDB = sqlite3.connect("Libary.db")
    cursor = LibaryDB.cursor()
    book_id = random.randint(1, 10000)
    cursor.execute("INSERT INTO books (book_id, title, author, year)"
                   "VALUES (?, ?, ?, ?)", (book_id, title, author, year))
    LibaryDB.commit()
    LibaryDB.close()

def add_reader(name, phone):
    LibaryDB = sqlite3.connect("Libary.db")
    cursor = LibaryDB.cursor()
    reader_id = random.randint(1, 10000)
    cursor.execute("INSERT INTO readers (reader_id, name, phone)"
                   "VALUES (?, ?, ?)", (reader_id, name, phone))
    LibaryDB.commit()
    LibaryDB.close()

def give_book(reader_id, book_id):
    LibaryDB = sqlite3.connect("Libary.db")
    cursor = LibaryDB.cursor()
    cursor.execute("UPDATE books SET available=? WHERE book_id=?", (0, book_id))
    cursor.execute("UPDATE readers SET book_id= book_id+? WHERE reader_id=?", (book_id, reader_id))
    LibaryDB.commit()
    LibaryDB.close()

def return_book(book_id):
    LibaryDB = sqlite3.connect("Libary.db")
    cursor = LibaryDB.cursor()
    cursor.execute("UPDATE books SET available=? WHERE book_id=?", (1, book_id))
    cursor.execute("UPDATE readers SET book_id=? WHERE book_id=?", ("empty", book_id))
    LibaryDB.commit()
    LibaryDB.close()

def get_available_books():
    LibaryDB = sqlite3.connect("Libary.db")
    cursor = LibaryDB.cursor()
    books = cursor.execute("SELECT * FROM books WHERE available=1")
    for book in books:
        print(book)
    LibaryDB.commit()
    LibaryDB.close()

def get_reader_books(reader_id):
    LibaryDB = sqlite3.connect("Libary.db")
    cursor = LibaryDB.cursor()
    books = cursor.execute("SELECT books_id FROM books WHERE reader_id=?", (reader_id))
    for book in books:
        print(book)
    LibaryDB.commit()
    LibaryDB.close()

def search_books(keyword):
    libraryDB = sqlite3.connect("Libary.db")
    cursor = libraryDB.cursor()
    c = int(input("Search by 1) name or 2) author: "))
    match c:
        case 1:
            books = cursor.execute("SELECT * from books WHERE title=?", (keyword,))
            for book in books:
                print(book)
        case 2:
            books = cursor.execute("SELECT * from books WHERE author=?", (keyword,))
            for book in books:
                print(book)
    libraryDB.close()


while True:
    print(f"Choose act: \n"
          f"1)add_book \n"
          f"2)add_reader \n"
          f"3)give_book \n"
          f"4)return_book \n"
          f"5)get_available_books \n"
          f"6)get_reader_books \n"
          f"7)search_books")
    act = int(input())
    match act:
        case 1:
            title = input("title: ")
            author = input("author: ")
            year = int(input("year: "))
            add_book(title, author, year)
        case 2:
            name = input("name: ")
            phone = input("phone: ")
            add_reader(name, phone)
        case 3:
            reader_id = input("reader_id: ")
            book_id = input("book_id: ")
            give_book(reader_id, book_id)
        case 4:
            book_id = input("book_id: ")
            return_book(book_id)
        case 5:
            get_available_books()
        case 6:
            reader_id = int(input("reader_id: "))
            get_reader_books(reader_id)
        case 7:
            keyword = input("Keyword: ")
            search_books(keyword)


