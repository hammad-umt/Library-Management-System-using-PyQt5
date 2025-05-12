# 📚 Library Management System (GUI using PyQt5)

This is a Python-based desktop application for managing a library's physical books and ebooks. Built using **PyQt5** for the graphical user interface (GUI), the application allows users to perform various actions such as adding, removing, lending, returning, and searching books, along with viewing the status of available and lent books.

## 🧰 Features
- Add physical books and ebooks to the library
- Remove books by ISBN
- Lend and return books
- Search books by author
- View available and lent books
- Toggle between physical books and ebooks using a checkbox
- Interactive and user-friendly PyQt5 interface

## 🖼️ GUI Overview
- Clean, modern layout with labeled input fields
- Optional fields for eBooks (Format and Size)
- Buttons for adding/removing books, lending/returning, and searching
- Message boxes to show success/failure and book listings
- Responsive and intuitive design

## 📦 Requirements
- Python 3.x
- PyQt5 (install via `pip install PyQt5`)
- A custom module `library_logic.py` (must be in the same directory)

## 📁 File Structure
LibraryManagementSystem
- app_gui.py - Main GUI code using PyQt5
- library_logic.py - Contains classes: Book, Ebook, Library, DigitalLibrary
- README.md - This file

## 🚀 How to Run
1. Make sure you have Python installed.
2. Install PyQt5 by running:
   ```bash
   pip install PyQt5
3. Ensure library_logic.py is present in the same folder.
4. Run the application:
   ```bash
      python app_gui.py
