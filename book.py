
class Book:
    def __init__(self):
        self.title, self.author = None, None

    def get_title(self):
        return "Title"

    def get_author(self):
        return self.author


PP, H, WP = Book(), Book(), Book()
PP.title, H.title, WP.title = "Jane Austin", "Hamlet", "War and Peace"
PP.author, H.author, WP.author = "J.K Rowling", "William Shakespeare", "Leo"
