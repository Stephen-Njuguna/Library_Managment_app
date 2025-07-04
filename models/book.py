class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author  
        self.year = year
        self.available = available

    def mark_available(self):
        self.available = True

    def mark_not_available(self):
        self.available = False

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"Book Title:{self.title}, Author:{self.author}, Publish year: {self.year} is {status}"


def main():
    book1 = Book("The Alchemist", "Pharmacist", 2020)
    book2 = Book("The Heist", "The Professor", 2021)

    print(book1)
    print(book2)

    print(f'Debug------Change of status Not Available-----')
    book1.mark_not_available()
    print(book1)
    print(f'Debug------Change of status Available-----')
    book1.mark_available()
    print(book1)


if __name__ == '__main__':  
    main()