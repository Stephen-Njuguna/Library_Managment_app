from .book import Book
from .student import Student
import sys
sys.path.append(r'C:\Library_Managment_App')
from utils.file_handler import save_book_to_json, save_student_to_json, save_borrowed_data_json, update_borrowed_data_json

class Library:
    def __init__(self):
        self.books = []
        self.students = []

    def add_books(self, book):
        if any(book.title.lower() == b.title.lower() for b in self.books):
            print(f'{book.title} already exists.')
        else:
            self.books.append(book)
            save_book_to_json(book)

    def register_student(self, student):
        if any(student.name.lower() == s.name.lower() for s in self.students):
            print(f'{student.name} already exists.')
        else:
            self.students.append(student)
            save_student_to_json(student)

    def borrow_book(self, student, book, due_date):
        name_student = next((s for s in self.students if s.name.lower() == student.name.lower()), None)
        title_book = next((b for b in self.books if b.title.lower() == book.title.lower()), None)

        if name_student and title_book:
            name_student.borrow_book(book, due_date)  
            save_book_to_json(book)
            save_borrowed_data_json(student, book, due_date)
        else:
            print('Book or Student not found')

    def return_book(self, book_title, book, student):
        name_student = next((s for s in self.students if s.name.lower() == student.name.lower()), None)

        if name_student:
            name_student.return_book(book_title, book)  
            save_book_to_json(book)
            update_borrowed_data_json(student, book_title)
        else:
            print(f"{student.name} has not borrowed '{book_title}'")

def main():
    library = Library()

    book1 = Book("The Alchemist", "Pharmacist", 2020)
    book2 = Book("The Heist", "The Professor", 2021)

    student1 = Student("John", "Medicine", 2025)
    student2 = Student("Doe", "History", 2010)

    library.add_books(book1)
    library.add_books(book2)  
    library.register_student(student1)
    library.register_student(student2)

    library.borrow_book(student1, book2, "04/07/2025")
    library.borrow_book(student2, book2, "05/07/2025")
    library.return_book("The Heist", book2, student2)

if __name__ == '__main__':
    main()