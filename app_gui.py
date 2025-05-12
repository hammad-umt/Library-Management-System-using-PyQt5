import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox, QFormLayout
from PyQt5.QtCore import Qt
from library_logic import Book, Ebook, DigitalLibrary, Library

class LibraryManagementSystem(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Library Management System")
        self.setGeometry(100, 100, 750, 600)
        self.setStyleSheet("background-color: #f0f0f0;")
        
        # Create library objects
        self.library = Library()
        self.dlibrary = DigitalLibrary()
        self.setup_initial_data() 
        # Set up the layout
        main_layout = QVBoxLayout()
        header_layout = QHBoxLayout()

        title_label = QLabel("Welcome to the Library Management System")
        title_label.setStyleSheet("font: 20px Arial; color: white; background-color: #007ACC; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(title_label)

        # Form layout for book input
        form_layout = QFormLayout()
        self.b_name = QLineEdit(self)
        self.a_name = QLineEdit(self)
        self.isbn = QLineEdit(self)
        self.book_size = QLineEdit(self)
        self.book_format = QLineEdit(self)

        self.b_name.setPlaceholderText("Enter Book Title")
        self.a_name.setPlaceholderText("Enter Author Name")
        self.isbn.setPlaceholderText("Enter ISBN")
        self.book_size.setPlaceholderText("Enter Book Size (MB)")
        self.book_format.setPlaceholderText("Enter Book Format (PDF, EPUB, MOBI)")

        form_layout.addRow("Enter Book Title:", self.b_name)
        form_layout.addRow("Enter Author Name:", self.a_name)
        form_layout.addRow("Enter ISBN:", self.isbn)

        # eBook checkbox
        self.ebook_checkbox = QCheckBox("Is this an eBook?")
        self.ebook_checkbox.setStyleSheet("font: 12px Arial; color: #007ACC;")
        self.ebook_checkbox.stateChanged.connect(self.toggle_ebook_fields)
        form_layout.addRow(self.ebook_checkbox)

        # Initially disable eBook fields
        self.book_size.setDisabled(True)
        self.book_format.setDisabled(True)
        form_layout.addRow("Enter Book Size (in MB):", self.book_size)
        form_layout.addRow("Enter Book Format (PDF, EPUB, MOBI):", self.book_format)

        # Buttons Layout
        buttons_layout = QVBoxLayout()
        
        self.add_button = QPushButton("1. Add Book")
        self.add_button.setStyleSheet("background-color: #007ACC; color: white; font: 12px Arial; padding: 10px;")
        self.add_button.clicked.connect(self.add_book)

        self.remove_button = QPushButton("2. Remove Book")
        self.remove_button.setStyleSheet("background-color: #007ACC; color: white; font: 12px Arial; padding: 10px;")
        self.remove_button.clicked.connect(self.remove_book)

        self.lend_button = QPushButton("3. Lend Book")
        self.lend_button.setStyleSheet("background-color: #007ACC; color: white; font: 12px Arial; padding: 10px;")
        self.lend_button.clicked.connect(self.lend_book)

        self.return_button = QPushButton("4. Return Book")
        self.return_button.setStyleSheet("background-color: #007ACC; color: white; font: 12px Arial; padding: 10px;")
        self.return_button.clicked.connect(self.return_book)

        self.show_all_button = QPushButton("5. Show All Available Books")
        self.show_all_button.setStyleSheet("background-color: #007ACC; color: white; font: 12px Arial; padding: 10px;")
        self.show_all_button.clicked.connect(self.show_all_books)

        self.show_lent_button = QPushButton("6. Show All Lent Books")
        self.show_lent_button.setStyleSheet("background-color: #007ACC; color: white; font: 12px Arial; padding: 10px;")
        self.show_lent_button.clicked.connect(self.show_lent_books)

        self.search_button = QPushButton("7. Search Books by Author")
        self.search_button.setStyleSheet("background-color: #007ACC; color: white; font: 12px Arial; padding: 10px;")
        self.search_button.clicked.connect(self.search_books_by_author)

        self.exit_button = QPushButton("0. Exit")
        self.exit_button.setStyleSheet("background-color: #FF6347; color: white; font: 12px Arial; padding: 10px;")
        self.exit_button.clicked.connect(self.close)

        # Add buttons to the layout
        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.remove_button)
        buttons_layout.addWidget(self.lend_button)
        buttons_layout.addWidget(self.return_button)
        buttons_layout.addWidget(self.show_all_button)
        buttons_layout.addWidget(self.show_lent_button)
        buttons_layout.addWidget(self.search_button)
        buttons_layout.addWidget(self.exit_button)

        # Main Layout
        main_layout.addLayout(header_layout)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

   
    def setup_initial_data(self):
        self.library.addBook(Book("Raja Gidh", "Bano Qudsia", "9789693502012"))
        self.library.addBook(Book("Peer-e-Kamil", "Umera Ahmed", "9789690014563"))
        self.library.addBook(Book("Aangan", "Khadija Mastoor", "9789692104378"))
        self.library.addBook(Book("Zavia", "Ashfaq Ahmed", "9789693501961"))
        self.library.addBook(Book("Udas Naslain", "Abdullah Hussain", "9789690017007"))
        self.dlibrary.addEbook(Ebook("Shehr-e-Zaat", "Umera Ahmed", "9789690023329", "PDF"))
        self.dlibrary.addEbook(Ebook("Mushaf", "Umera Ahmed", "9789692109878", "EPUB"))
        self.dlibrary.addEbook(Ebook("Amarbail", "Umera Ahmed", "9789690017325", "MOBI"))
        self.dlibrary.addEbook(Ebook("Hasil", "Umera Ahmed", "9789693502981", "PDF"))
        self.dlibrary.addEbook(Ebook("Mirat-ul-Uroos", "Deputy Nazir Ahmad", "9789692109876", "EPUB"))

    def toggle_ebook_fields(self):
        if self.ebook_checkbox.isChecked():
            self.book_size.setEnabled(True)
            self.book_format.setEnabled(True)
        else:
            self.book_size.setDisabled(True)
            self.book_format.setDisabled(True)

    def add_book(self):
        if self.ebook_checkbox.isChecked():
            ebook = Ebook(self.b_name.text(), self.a_name.text(), self.isbn.text(), self.book_size.text())
            self.dlibrary.addEbook(ebook)
            QMessageBox.information(self, "Success", "Ebook added successfully!")
        else:
            book = Book(self.b_name.text(), self.a_name.text(), self.isbn.text())
            self.library.addBook(book)
            QMessageBox.information(self, "Success", "Book added successfully!")

    def remove_book(self):
        if self.ebook_checkbox.isChecked():
            for ebook in self.dlibrary.ebooks:
                if ebook.ISBN == self.isbn.text():
                    self.dlibrary.removeEbook(ebook)
                    QMessageBox.information(self, "Success", "Ebook removed successfully!")
                    break
        else:
            for book in self.library.books:
                if book.ISBN == self.isbn.text():
                    self.library.removeBook(book)
                    QMessageBox.information(self, "Success", "Book removed successfully!")
                    break

    def lend_book(self):
        if self.ebook_checkbox.isChecked():
            for ebook in self.dlibrary.ebooks:
                if ebook.ISBN == self.isbn.text():
                    try:
                        self.dlibrary.lendEbook(ebook)
                        QMessageBox.information(self, "Success", "Ebook lent successfully!")
                    except Exception as e:
                        QMessageBox.warning(self, "Error", str(e))
                    break
        else:
            for book in self.library.books:
                if book.ISBN == self.isbn.text():
                    try:
                        self.library.lendBook(book)
                        QMessageBox.information(self, "Success", "Book lent successfully!")
                    except Exception as e:
                        QMessageBox.warning(self, "Error", str(e))
                    break

    def return_book(self):
        if self.ebook_checkbox.isChecked():
            for ebook in self.dlibrary.lent_books:
                if ebook.ISBN == self.isbn.text():
                    self.dlibrary.returnEbook(ebook)
                    QMessageBox.information(self, "Success", "Ebook returned successfully!")
                    break
        else:
            for book in self.library.lent_books:
                if book.ISBN == self.isbn.text():
                    self.library.returnBook(book)
                    QMessageBox.information(self, "Success", "Book returned successfully!")
                    break

    def show_all_books(self):
        books = self.library.displayBooks() or []
        ebooks = self.dlibrary.displayEbooks() or []
        if not books and not ebooks:
            QMessageBox.information(self, "Available Books", "No books available.")
            return

        all_books = "Available Physical Books:\n"
        for book in books:
            all_books += f"{str(book)}\n"

        all_books += "\nAvailable Ebooks:\n"
        for ebook in ebooks:
            all_books += f"{str(ebook)}\n"

        QMessageBox.information(self, "Library Books", all_books)

    def show_lent_books(self):
        lent_books = self.library.displayLentBooks() or []
        lent_ebooks = self.dlibrary.displayLentEbooks() or []
        if not lent_books and not lent_ebooks:
            QMessageBox.information(self, "Lent Books", "No books are currently lent out.")
            return

        all_lent_books = "Lent Physical Books:\n"
        for book in lent_books:
            all_lent_books += f"{str(book)}\n"

        all_lent_books += "\nLent Ebooks:\n"
        for ebook in lent_ebooks:
            all_lent_books += f"{str(ebook)}\n"

        QMessageBox.information(self, "Lent Books", all_lent_books)

    def search_books_by_author(self):
        author_name = self.a_name.text()
        books = self.library.displayBookbyAuthor(author_name) or []
        ebooks = self.dlibrary.displayEbookbyAuthor(author_name) or []
        if not books and not ebooks:
            QMessageBox.information(self, "Search Result", "No books found by this author.")
            return
        search_result = "Books by Author:\n"
        for book in books:
            search_result += f"{str(book)}\n"
        search_result += "\nEbooks by Author:\n"
        for ebook in ebooks:
            search_result += f"{str(ebook)}\n"
        QMessageBox.information(self, "Search Result", search_result)
   
   

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LibraryManagementSystem()
    window.show()
    sys.exit(app.exec_())
