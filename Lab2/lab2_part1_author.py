class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        if self.books:
            book_list = ', '.join(self.books)
        else:
            book_list = 'No books'

        # book_list = ', '.join(self.books) or 'No published books'
        # this code does the same thing as code above. print 'No published books' if the variable is falsy value

        return f'Author Name: {self.name}\nPublished Books: {book_list}'

    def publish(self, title):

        # When the publish method is called,
        # print an error message if the book given has the same name as a book currently in the books list.
        # Do not add the duplicate book. (In other words, make sure the Author object's book list doesn't already contain that name).

        books_in_lowercase = []
        for book in self.books:
            books_in_lowercase.append(book.lower())

        if title.lower() in books_in_lowercase:
            print('This book is already in the published book list.')
        else:
            self.books.append(title)

author1 = Author('Sally Rooney')

print(author1)

author1.publish('Normal People')
author1.publish('Conversations with Friends')

print(author1)

author1.publish('Normal People')

print(author1)