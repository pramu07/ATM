CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE,
    phone TEXT
);

CREATE TABLE Books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    genre TEXT,
    isbn TEXT UNIQUE,
    available INTEGER
);

CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    book_id INTEGER,
    borrow_date DATE,
    return_date DATE,
    due_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users (user_id),
    FOREIGN KEY (book_id) REFERENCES Books (book_id)
);

# Define classes for User, Book, and Library.
# Implement methods for CRUD operations and transaction management
class User:
    def __init__(self, user_id, name, email, phone):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone

class Book:
    def __init__(self, book_id, title, author, genre, isbn, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.available = available

class Library:
    def __init__(self, db_connection):
        self.conn = db_connection
        self.cursor = self.conn.cursor()

    def add_user(self, user):
        # Implement SQL INSERT query to add user
        pass

    def add_book(self, book):
        # Implement SQL INSERT query to add book
        pass

    def borrow_book(self, user_id, book_id):
        # Implement logic to borrow book and update records
        pass

    def return_book(self, user_id, book_id):
        # Implement logic to return book and update records
        pass

    def search_books(self, **kwargs):
        # Implement logic to search for books based on criteria
        pass


import sqlite3
from datetime import datetime, timedelta
class Library:
    def __init__(self, db_connection):
        self.conn = db_connection
        self.cursor = self.conn.cursor()

    def add_user(self, user):
        try:
            self.cursor.execute("INSERT INTO Users (name, email, phone) VALUES (?, ?, ?)",
                                (user.name, user.email, user.phone))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Error: User with this email already exists.")

    def add_book(self, book):
        try:
            self.cursor.execute("INSERT INTO Books (title, author, genre, isbn, available) VALUES (?, ?, ?, ?, ?)",
                                (book.title, book.author, book.genre, book.isbn, book.available))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Error: Book with this ISBN already exists.")

    def borrow_book(self, user_id, book_id):
        try:
            self.cursor.execute("SELECT available FROM Books WHERE book_id = ?", (book_id,))
            available = self.cursor.fetchone()[0]
            if available:
                borrow_date = datetime.now()
                due_date = borrow_date + timedelta(days=14)
                self.cursor.execute("INSERT INTO Transactions (user_id, book_id, borrow_date, due_date) VALUES (?, ?, ?, ?)",
                                    (user_id, book_id, borrow_date, due_date))
                self.cursor.execute("UPDATE Books SET available = 0 WHERE book_id = ?", (book_id,))
                self.conn.commit()
            else:
                print("Error: Book is not available.")
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def return_book(self, user_id, book_id):
        try:
            return_date = datetime.now()
            self.cursor.execute("UPDATE Transactions SET return_date = ? WHERE user_id = ? AND book_id = ? AND return_date IS NULL",
                                (return_date, user_id, book_id))
            self.cursor.execute("UPDATE Books SET available = 1 WHERE book_id = ?", (book_id,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def search_books(self, title=None, author=None, genre=None, isbn=None):
        query = "SELECT * FROM Books WHERE 1=1"
        params = []
        if title:
            query += " AND title LIKE ?"
            params.append(f"%{title}%")
        if author:
            query += " AND author LIKE ?"
            params.append(f"%{author}%")
        if genre:
            query += " AND genre LIKE ?"
            params.append(f"%{genre}%")
        if isbn:
            query += " AND isbn = ?"
            params.append(isbn)
        self.cursor.execute(query, tuple(params))
        return self.cursor.fetchall()
