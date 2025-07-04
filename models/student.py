from .book import Book

class Student:
    def __init__(self, name, department, year):
        self.name = name
        self.department = department
        self.year = year
        self.borrowed_books = []

    def borrow_book(self, book: Book, due_date):
        if book.available:
            self.borrowed_books.append((book,due_date))
            book.mark_not_available()
            return True
        return False
    
    def return_book(self, book_title, book: Book):
        for b,_ in self.borrowed_books:
            if b.title.lower() == book_title.lower():
                self.borrowed_books.remove((b, _))
                book.mark_available()
            return True
        return False
    
    def __str__(self):
        return f'student: {self.name}, Department: {self.department}, Year: {self.year}, Borrowed_books: {self.borrowed_books} - has been added'
    
def main():
    book1 = Book("The Alchemist", "Pharmacist", 2020)
    book2 = Book("The Heist", "The Professor", 2021)

    student1 = Student("John", "Medicine", 2025)
    student2 = Student("Doe", "History", 2010)

    print(student1)
    print(student2)

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

if __name__ == "__main__":
    main()