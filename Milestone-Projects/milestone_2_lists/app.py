from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def prompt_add_book():
    name = input('Enter name of book: ')
    author = input('Enter the author: ')
    database.add_book(name, author)

def list_books():
    books = database.get_all_books()
    for book in books:
        print(f"{book['name']} by {book['author']}, Read: {book['read']}")

def prompt_read_book():
    read_book = input('Enter the book you have read: ')
    database.read_book(read_book)

def prompt_delete_book():
    delete_book = input('Enter the book you want to delete: ')
    database.delete_book(delete_book)


user_options = {
    "a": prompt_add_book,
    "l": list_books,
    "r": prompt_read_book,
    "d": prompt_delete_book
}

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in user_options:
            selected_function = user_options[user_input]
            selected_function()
        else:
            print('Invalid choice')

        user_input = input(USER_CHOICE)


menu()