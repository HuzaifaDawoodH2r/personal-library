
import json

class BookCollection:
    """A class representing a collection of books."""

    def __init__(self):
        """Initialize a new book collection with an empty list and a file for storage."""
        self.book_list = []
        self.storage_file = "book_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load the saved books from a JSON file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        with open(self.storage_file, "w") as file:  # Fix: mode should be "w", not "r"
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection by gathering information from a user."""
        book_title = input("Enter book title: ")
        book_author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read
        }
        self.book_list.append(new_book)
        self.save_to_file()
        print("Book added successfully!\n")

    def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("Enter the title of the book to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return
        print("Book not found.\n")

    def find_book(self):
        """Search for books in the collection by title or author name."""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice (1 or 2): ")
        search_text = input("Enter search term: ").lower()

        if search_type == "1":
            found_books = [book for book in self.book_list if search_text in book["title"].lower()]
        elif search_type == "2":
            found_books = [book for book in self.book_list if search_text in book["author"].lower()]
        else:
            print("Invalid search type.\n")
            return

        if found_books:
            print("Matching books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}")
        else:
            print("No books found.\n")

    def start_application(self):
        while True:
            print("\nWelcome to your Book Collection!")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Exit")

            user_choice = input("Please choose an option (1-4): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Uncomment this to run the application
if __name__ == "__main__":
    app = BookCollection()
    app.start_application()


