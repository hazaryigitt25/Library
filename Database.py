import sqlite3
from datetime import date, timedelta


class Book():
    def __init__(self, name, writer, person, date1, date2):
        self.name = name
        self.writer = writer
        self.person = person
        self.date1 = date1
        self.date2 = date2

class Library():
    def __init__(self):
        self.make_connection()
    def make_connection(self):
        self.connection = sqlite3.connect("Library.db")
        self.cursor = self.connection.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS Books(Book TEXT, Writer TEXT, Person TEXT, Given_Date TEXT, Delivery_Date TEXT)"
        self.cursor.execute(sorgu)
        self.connection.commit()
    def cut_connection(self):
        self.connection.close()
    def add_book(self,book,writer,person):
        sorgu = "INSERT INTO Books VALUES(?,?,?,?,?)"
        given_date = date.today().isoformat()
        delivery_date = (date.today()+timedelta(days = 60)).isoformat()
        self.cursor.execute(sorgu,(book,writer,person,given_date,delivery_date))
        self.connection.commit()
        return True
    def delete_book(self,book,person):
        sorgu = "DELETE FROM Books WHERE Book = ? and Person = ?"
        self.cursor.execute(sorgu,(book,person))
        return True
    def all_list(self):
        sorgu = "SELECT * FROM Books"
        self.cursor.execute(sorgu)
        list = self.cursor.fetchall()
        return list
    def search_book(self,book,person):
        sorgu = "SELECT * FROM Books WHERE Book = ? and Person = ?"
        self.cursor.execute(sorgu,(book,person))
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            return False
        else:
            return True