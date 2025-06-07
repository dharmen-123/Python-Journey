# bookstore.py

class BookStore:
    def _init_(self):
        # Dictionary of book titles and their prices
        self.books = {
            "Python Programming": 599,
            "AI Basics": 699,
            "Data Science": 799
        }

    def search_book(self, title):
        """
        Search for a book by title.
        Returns availability message with price if found,
        else returns 'Book not available'.
        """
        if title in self.books:
            return f"{title} is available for ₹{self.books[title]}"
        else:
            return "Book not available"