# class ShoppingCart:
#      d={}
#      def additem():
#         pass
 

class Book:
    def __init__(self, book_id, title, author, price, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def _str_(self):
        return f"{self.book_id}: '{self.title}' by {self.author} - ${self.price} ({self.quantity} left)"


class Bookstore:
    def __init__(self):
        self.books = []
        self.cart = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book)

    def search_book(self, keyword):
        print(f"\nSearch results for '{keyword}':")
        found = False
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(book)
                found = True
        if not found:
            print("No matching books found.")

    def buy_book(self, book_id, quantity):
        for book in self.books:
            if book.book_id == book_id:
                if book.quantity >= quantity:
                    self.cart.append((book, quantity))
                    book.quantity -= quantity
                    print(f"Added {quantity} x '{book.title}' to cart.")
                    return
                else:
                    print("Not enough quantity available.")
                    return
        print("Book not found.")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
            return
        print("\nYour Cart:")
        total = 0
        for book, qty in self.cart:
            print(f"{qty} x {book.title} = ${qty * book.price}")
            total += qty * book.price
        print(f"Total: ${total:.2f}")

    def checkout(self):
        self.view_cart()
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("Thank you for your purchase!")
            self.cart = []
        else:
            print("Checkout canceled.")


# Sample usage
def main():
    store = Bookstore()
    store.add_book(Book(1, "The Great Gatsby", "F. Scott Fitzgerald", 10.99, 5))
    store.add_book(Book(2, "1984", "George Orwell", 8.99, 3))
    store.add_book(Book(3, "To Kill a Mockingbird", "Harper Lee", 9.99, 4))

    while True:
        print("\n--- Online Bookstore Menu ---")
        print("1. List all books")
        print("2. Search for a book")
        print("3. Buy a book")
        print("4. View cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            store.list_books()
        elif choice == '2':
            keyword = input("Enter title or author to search: ")
            store.search_book(keyword)
        elif choice == '3':
            try:
                book_id = int(input("Enter Book ID to buy: "))
                quantity = int(input("Enter quantity: "))
                store.buy_book(book_id, quantity)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            store.view_cart()
        elif choice == '5':
            store.checkout()
        elif choice == '6':
            print("Thank you for visiting the bookstore!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()