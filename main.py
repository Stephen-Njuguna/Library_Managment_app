from models.book import Book
from models.student import Student
from models.library import Library
import sys
sys.path.append(r'C:\Library_Managment_App')
from utils.file_handler import save_book_to_json, save_student_to_json, save_borrowed_data_json, update_borrowed_data_json

def main():
    # File_handler test 
    book1 = Book("Test book", "author", 2018)
    book2 = Book("Best Seller", "best Author", 2017)
    book3 = Book("The Alchemist", "Pharmacist", 2020)
    book4 = Book("The Heist", "The Professor", 2021)

    student1 = Student("test student", "research", 2020)
    student2 = Student("test3 student", "research", 2020)
    student3 = Student("John", "Medicine", 2025)
    student4 = Student("Doe", "History", 2010)

    save_student_to_json(student1)
    save_student_to_json(student2)

    save_borrowed_data_json(student1, book2, "03/07/2025")
    save_borrowed_data_json(student2, book2, "07/10/2025")

    #Book Test 
    
    print(book1)
    print(book2)

    print(f'Debug------Change of status Not Available-----')
    book1.mark_not_available()
    print(book1)
    print(f'Debug------Change of status Available-----')
    book1.mark_available()
    print(book1)

    

    print(f'Debug ---- borrowed Books-------------')
    student2.borrow_book(book1,"7/03/2025")
    print(student2)
    print(book1)

    print(f'Debug ---- Return Books = True-------------')
    student2.return_book("The Alchemist",book1)
    print(student2)
    print(book1)

    print(f'Debug ---- Return Books = False-------------')
    student1.return_book("The Heist", book2)

    #Library Test 
    library = Library()

 
    library.add_books(book1)
    library.add_books(book2) 
    library.add_books(book4)
    library.add_books(book3) 

    library.register_student(student1)
    library.register_student(student2)

    library.borrow_book(student1, book2, "04/07/2025")
    library.borrow_book(student2, book2, "05/07/2025")
    # library.return_book("The Heist", book2, student2)

   
if __name__ == '__main__':
    main()