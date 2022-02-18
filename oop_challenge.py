"""
Bookshelf, Books, Magazine and Notebooks Classes (Python3)
"""


class NoteBook(object):
    def __init__(self):
        self.owner = ""


class Magazine(object):
    def __init__(self):
        self.name = ""
        self.publicationDate = ""


class Book(object):
    def __init__(self):
        self.title = ""
        self.author = ""

    def store(self, bookData):
        # store book operation
        book = []
        return book  # success

    def retrieve(self, bookId):
        # retrieve book data
        book = []
        return book

    def read(self, bookId, pageNumber):
        # read the page content given page number
        contents = ""
        return contents


class BookShelf(Book):

    def checkState(self):
        # retrieve and manipulate the state of the bookshelf
        state = {'used': 5, 'available': 12}
        return state

    def search(self, content):
        # search for the contents from content parameter
        contents = ""
        return contents
