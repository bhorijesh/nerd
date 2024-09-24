class book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"book '{self.title}' is available")
        else:
            print(f"book '{self.title}' is not available")

    def return_book(self):
        self.available_copies += 1
        print(f"book '{self.title}' is returned")


class member:
    def __init__(self, member_id, name, borrowed_books=None):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def borrow_books(self, book):
        if len(self.borrowed_books) < 3:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print("you have borrowed 3 books already")

    def return_books(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"member '{self.name}' has not borrowed the book")


class library:
    def __init__(self):
        self.book = []
        self.member = []

    def add_book(self, book):
        self.book.append(book)
        print(f"Book '{book.title}' added to library")

    def add_member(self, member):
        self.member.append(member)
        print(f"member '{member.name}' has been added to library")

    def issue_book(self, member, book):
        if book in self.book and member in self.member:
            if book.available_copies > 0:
                member.borrow_books(book)
            else:
                print(f"book '{book.title}' is not available")
        else:
            print(f"member '{member.name}' is not found")

    def return_book(self, member, book):
        if book in self.book and member in self.member:
            member.return_books(book)
        else:
            print("Book or member not found")
    

book1 = book("The Catcher in the Rye", "J.D. Salinger", "1234567890", 3)
book2 = book("To Kill a Mockingbird", "Harper Lee", "0987654321", 2)
book3 = book("1984", "George Orwell", "1122334455", 1)

member1 = member("Ram", "M001")
member2 = member("shyam", "M002")
member3 = member("hari", "M003")

library = library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_member(member1)
library.add_member(member2)
library.add_member(member3)


print("\n-- Transaction 1: Alice borrows 'The Catcher in the Rye' --")
library.issue_book(member1, book1)

print("\n-- Transaction 2:ram returns 'The Catcher in the Rye' --")
library.return_book(member1, book1)

print("\n-- Transaction 3: shyam tries to borrow '1984', which has 1 copy --")
library.issue_book(member2, book3)

print("\n-- Transaction 4: hari tries to borrow '1984', but it's unavailable --")
