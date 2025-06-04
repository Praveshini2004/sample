import requests

# Base URL of the FastAPI server
Base_url = "http://127.0.0.1:8020"

def create_publisher():
    """Function to create a new publisher."""
    name = input("Enter publisher name: ")
    country = input("Enter publisher country: ")
    response = requests.post(f"{Base_url}/publishers/", json={"name": name, "country": country})
    if response.status_code == 200:
        print("Publisher created successfully!")
        print(response.json())
    else:
        print(f"Failed to create publisher: {response.json()}")

def list_publishers():
    """Function to list all publishers."""
    response = requests.get(f"{Base_url}/publishers/")
    if response.status_code == 200:
        publishers = response.json()
        if publishers:
            print("Publishers:")
            for publisher in publishers:
                print(f"ID: {publisher['id']}, Name: {publisher['name']}, Country: {publisher['country']}")
        else:
            print("No publishers found.")
    else:
        print(f"Failed to fetch publishers: {response.json()}")

def create_book():
    """Function to create a new book."""
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    price = float(input("Enter book price: "))
    stock = int(input("Enter book stock: "))
    publisher_id = int(input("Enter publisher ID: "))
    response = requests.post(f"{Base_url}/books/", json={
        "title": title,
        "author": author,
        "price": price,
        "stock": stock,
        "publisher_id": publisher_id
    })
    if response.status_code == 200:
        print("Book created successfully!")
        print(response.json())
    else:
        print(f"Failed to create book: {response.json()}")

def list_books():
    """Function to list all books."""
    response = requests.get(f"{Base_url}/books/")
    if response.status_code == 200:
        books = response.json()
        if books:
            print("Books:")
            for book in books:
                print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, "
                      f"Price: {book['price']}, Stock: {book['stock']}, Publisher ID: {book['publisher_id']}")
        else:
            print("No books found.")
    else:
        print(f"Failed to fetch books: {response.json()}")

def search_books():
    """Function to search for books by title or author."""
    title = input("Enter book title to search (leave blank to skip): ")
    author = input("Enter book author to search (leave blank to skip): ")
    params = {}
    if title:
        params["title"] = title
    if author:
        params["author"] = author
    response = requests.get(f"{Base_url}/books/search-books", params=params)
    if response.status_code == 200:
        books = response.json()
        if books:
            print("Search Results:")
            for book in books:
                print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, "
                      f"Price: {book['price']}, Stock: {book['stock']}, Publisher ID: {book['publisher_id']}")
        else:
            print("No books found matching the search criteria.")
    else:
        print(f"Failed to search books: {response.json()}")

def delete_book():
    """Function to delete a book by ID."""
    book_id = int(input("Enter the ID of the book to delete: "))
    response = requests.delete(f"{Base_url}/books/{book_id}")
    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print(f"Failed to delete book: {response.json()}")

def update_book():
    """Function to update a book's price and stock."""
    book_id = int(input("Enter the ID of the book to update: "))
    price = float(input("Enter the new price: "))
    stock = int(input("Enter the new stock: "))
    response = requests.put(f"{Base_url}/books/{book_id}", json={"price": price, "stock": stock})
    if response.status_code == 200:
        print("Book updated successfully!")
        print(response.json())
    else:
        print(f"Failed to update book: {response.json()}")

def menu():
    """Main menu for the client."""
    while True:
        print("\nBook Inventory Management")
        print("1. Create Publisher")
        print("2. List Publishers")
        print("3. Create Book")
        print("4. List Books")
        print("5. Search Books")
        print("6. Delete Book")
        print("7. Update Book")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_publisher()
        elif choice == "2":
            list_publishers()
        elif choice == "3":
            create_book()
        elif choice == "4":
            list_books()
        elif choice == "5":
            search_books()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            update_book()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
