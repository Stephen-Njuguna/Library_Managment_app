

library_Managment_app/                    # Root folder (your project)
│
├── models/                     # Contains all class definitions
│   ├── __init__.py             # Makes this a Python package
│   ├── book.py                 # Book class
│   ├── student.py              # Student class
│   └── library.py              # Library class
│
├── data/                       # Folder to store your text and json files
│   ├── books.txt               # Saved book records
│   ├── students.txt            # Saved student records
│   └── borrowed.json           # JSON record of borrowed books
│
├── utils/                      # Helper functions for saving/loading files
│   ├── __init__.py
│   ├── file_handler.py         # For reading/writing .txt and .json
│
├── main.py                     # Main entry point of the app
└── README.md                   # (Optional) Project description
