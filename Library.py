from Database import *
from PyQt5.QtWidgets import QTableWidget, QFormLayout,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton, QApplication,QWidget, QTableWidgetItem

atm = Library()
class Library(QWidget):
    def  __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Library")

        self.MainLayout = QHBoxLayout()

        # Creating Buttons
        self.add_button = QPushButton('Add Book')
        self.delete_button = QPushButton('Delete Book')
        
        # Creating Lines
        self.book_name = QLineEdit()
        self.book_writer = QLineEdit()
        self.who_gives = QLineEdit()
        self.who_deletes = QLineEdit()
        self.book_name_taken = QLineEdit()

        # Creating Labels
        book_name_label = QLabel("Book Name:")
        book_writer_label = QLabel("Writer:")
        who_gives_label = QLabel("Your Name:")
        who_deletes_label = QLabel("Your Name:")
        book_name_taken_label = QLabel("Book Name:")
        self.error_message = QLabel("")
        # Setting Layout
        
        rightside_layout = QVBoxLayout()
        
        rightside_layout1 = QHBoxLayout()
        rightside_layout1.addStretch()
        rightside_layout1.addWidget(who_gives_label)
        rightside_layout1.addWidget(self.who_gives)

        rightside_layout2 = QHBoxLayout()
        rightside_layout2.addStretch()
        rightside_layout2.addWidget(book_name_label)
        rightside_layout2.addWidget(self.book_name)

        rightside_layout3 = QHBoxLayout()
        rightside_layout3.addStretch()
        rightside_layout3.addWidget(book_writer_label)
        rightside_layout3.addWidget(self.book_writer)

        rightside_layout4 = QHBoxLayout()
        rightside_layout4.addStretch()
        rightside_layout4.addWidget(self.add_button)

        rightside_layout5 = QHBoxLayout()
        rightside_layout5.addStretch()
        rightside_layout5.addWidget(self.error_message)

        rightside_layout6 = QHBoxLayout()
        rightside_layout6.addStretch()
        rightside_layout6.addWidget(who_deletes_label)
        rightside_layout6.addWidget(self.who_deletes)

        rightside_layout7 = QHBoxLayout()
        rightside_layout7.addStretch()
        rightside_layout7.addWidget(book_name_taken_label)
        rightside_layout7.addWidget(self.book_name_taken)

        rightside_layout8 = QHBoxLayout()
        rightside_layout8.addStretch()
        rightside_layout8.addWidget(self.delete_button)

        rightside_layout.addStretch()
        rightside_layout.addLayout(rightside_layout1)
        rightside_layout.addLayout(rightside_layout2)
        rightside_layout.addLayout(rightside_layout3)
        rightside_layout.addLayout(rightside_layout4)
        rightside_layout.addLayout(rightside_layout5)
        rightside_layout.addLayout(rightside_layout6)
        rightside_layout.addLayout(rightside_layout7)
        rightside_layout.addLayout(rightside_layout8)

        # Setting Headers
        self.header = ['Book Name','Writer','Your Name','Date Of Taken','Delivery Date']
        # Creating Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(self.header)
        self.book_list = atm.all_list()
        self.table.setRowCount(len(self.book_list))
        for i,books in enumerate(self.book_list):
            self.table.setItem(i, 0, QTableWidgetItem(books[0]))
            self.table.setItem(i, 1, QTableWidgetItem(books[1]))
            self.table.setItem(i, 2, QTableWidgetItem(books[2]))
            self.table.setItem(i, 3, QTableWidgetItem(books[3]))
            self.table.setItem(i, 4, QTableWidgetItem(books[4]))

        

        self.MainLayout.addWidget(self.table)
        self.MainLayout.addStretch()
        self.MainLayout.addLayout(rightside_layout)
        # Button Click Connections
        self.add_button.clicked.connect(self.add_book)
        self.delete_button.clicked.connect(self.delete_book)

        self.setLayout(self.MainLayout)
    
        self.show()
    
    def add_book(self):
        name1 = self.book_name.text()
        writer1 = self.book_writer.text()
        person1 = self.who_gives.text()
        if name1 == "" or writer1 == "" or person1 == "":
            self.error_message.setText("Please! Fill Line Correctly!")
        else:
            atm.add_book(name1,writer1,person1)
            self.close()
            self.book_list2 = atm.all_list()
            self.table.setRowCount(len(self.book_list2))
            for i,books in enumerate(self.book_list2):
                self.table.setItem(i, 0, QTableWidgetItem(books[0]))
                self.table.setItem(i, 1, QTableWidgetItem(books[1]))
                self.table.setItem(i, 2, QTableWidgetItem(books[2]))
                self.table.setItem(i, 3, QTableWidgetItem(books[3]))
                self.table.setItem(i, 4, QTableWidgetItem(books[4]))
            self.show()
            self.book_name.clear()
            self.book_writer.clear()
            self.who_gives.clear()
            self.error_message.setText("Process Worked Successfully :)")


    def delete_book(self):
        name1 = self.who_deletes.text()
        book1 = self.book_name_taken.text()
        durum = atm.search_book(book1,name1)
        if durum:
            atm.delete_book(book1,name1)
            self.close()
            self.book_list2 = atm.all_list()
            self.table.setRowCount(len(self.book_list2))
            for i,books in enumerate(self.book_list2):
                self.table.setItem(i, 0, QTableWidgetItem(books[0]))
                self.table.setItem(i, 1, QTableWidgetItem(books[1]))
                self.table.setItem(i, 2, QTableWidgetItem(books[2]))
                self.table.setItem(i, 3, QTableWidgetItem(books[3]))
                self.table.setItem(i, 4, QTableWidgetItem(books[4]))
            self.show()
            self.who_deletes.clear()
            self.book_name_taken.clear()
            self.error_message.setText("Process Worked Succesfully :)")
        else:
            self.error_message.setText("This Book Could Not Found :(")
 
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    library = Library()
    
    sys.exit(app.exec_())