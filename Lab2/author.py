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
        self.books.append(title)

author1 = Author('Sally Rooney')
author1.publish('Normal People')
author1.publish('Conversations with Friends')
print(author1)

author2 = Author('Hyungna Lim')
print(author2)
