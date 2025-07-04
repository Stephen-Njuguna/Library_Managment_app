import json
import os
import sys
sys.path.append(r'C:\Library_Managment_App')

from models.student import Student
from models.book import Book
# from models.library import Library

# Saving book/updating to json file
def save_book_to_json(book, file_path=r'C:\Library_Managment_App\data\books.json'):
    books = []

    if os.path.exists(file_path):
        with open(file_path, 'r') as b:
            try:
                books = json.load(b)
            except json.JSONDecodeError:
                books = [] 
            
    update = False

    for b_item in books:
        if b_item['title'].lower() == book.title.lower():
            b_item['available'] = book.available  
            update = True
            break

    if not update:
        books.append({
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'available': book.available
        })

    with open(file_path, 'w') as b:
        json.dump(books, b, indent=4)

# Saving students to json file
def save_student_to_json(student, file_path=r'C:\Library_Managment_App\data\students.json'):
    students = []
    entry = {
        "name": student.name,
        "department": student.department,
        "year": student.year
    }

    if os.path.exists(file_path):
        with open(file_path, 'r') as sf:
            try:
                students = json.load(sf)
            except json.JSONDecodeError:
                students = []
    
    if not any(s['name'].lower() == student.name.lower() for s in students):
        students.append(entry)
        with open(file_path, 'w') as sf:
            json.dump(students, sf, indent=4)
    else:
        print(f"student: {student.name.title()} already exists in JSON file")

# Save borrowed book
def save_borrowed_data_json(student, book, due_date, file_path=r'C:\Library_Managment_App\data\borrowed_data.json'):
    borrowed_data = []

    book_entry = {
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "due_date": due_date
    }

    data_student = {
        'name': student.name,
        'department': student.department,
        'year': student.year,
        'borrowed_books': [book_entry]
    }

    if os.path.exists(file_path):
        with open(file_path, 'r') as bd:
            try:
                borrowed_data = json.load(bd)
            except json.JSONDecodeError:
                borrowed_data = []

    if not any(student.name.lower() == data['name'].lower() for data in borrowed_data):
        borrowed_data.append(data_student)
    else:
        for entry in borrowed_data:
            if entry['name'].lower() == student.name.lower():  
                if any(book.title.lower() == e['title'].lower() for e in entry['borrowed_books']):
                    print(f"{student.name}! You have already borrowed {book.title}")
                else:
                    entry["borrowed_books"].append(book_entry)
                break  

    with open(file_path, 'w') as bd:
        json.dump(borrowed_data, bd, indent=4)

# Update borrowed data by removing book
def update_borrowed_data_json(student, book_title, file_path=r'C:\Library_Managment_App\data\borrowed_data.json'):
    if not os.path.exists(file_path):
        return print(f'Error: check borrowed_data file path')

    with open(file_path, 'r') as f:
        data = json.load(f)
     
        for entry in data:
            if student.name.lower() == entry['name'].lower():
                if any(book_title.lower() == e['title'].lower() for e in entry['borrowed_books']):
                    
                    entry['borrowed_books'] = [
                        book for book in entry['borrowed_books']
                        if book['title'].lower() != book_title.lower()]
                    print(f'{student.name} has returned {book_title}')
                else:
                    print(f'{student.name}, did not have {book_title} borrowed')
                break
        else:
            print(f'No borrowed record found for {student.name}.')

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Main test
def main():
    book1 = Book("Test book", "author", 2018)
    book2 = Book("Best Seller", "best Author", 2017)

    student1 = Student("test student", "research", 2020)
    student2 = Student("test3 student", "research", 2020)

    save_student_to_json(student1)
    save_student_to_json(student2)

    save_borrowed_data_json(student1, book2, "03/07/2025")
    save_borrowed_data_json(student2, book2, "07/10/2025")

    # update_borrowed_data_json(student1, "Best Seller")

if __name__ == '__main__':
    main()
