class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return (f'{self.title} by {self.author} on {self.year}')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f'Added {new_book} successfully!')

    def show_book(self):
        if not self.books:
            print('No books is here!')
        else:
            for i, book in enumerate(self.books, 1):
                print(f'{i}. {book.title} by {book.author}')

    def search_book(self, keyword):
        found = [book for book in self.books if keyword.lower() in book.title.lower()]
        if found:
            print('result of searching! :')
            for book in found:
                print(book)
        else:
            print('no result found!')

    def remove_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower():
                self.books.remove(book)
                print(f'Removed {book} successfully!')
                return
        print('no book with this name found!')


def main():
    library = Library()
    while True:
        print('welcome to my library!')
        print('1. Add a book')
        print('2. show all of books')
        print('3. search book')
        print('4. remove a book')
        print('5. exit')

        chose = input('Enter your choice: ')
        if chose == '1':
            title = input('Enter book title: ')
            author = input('Enter book author: ')
            year = input('Enter book year: ')
            library.add_book(title, author, year)
        elif chose == '2':
            library.show_book()

        elif chose == '3':
            keywords = input('Enter keywords: ')
            library.search_book(keywords)

        elif chose == '4':
            title = input('Enter book title: ')
            library.remove_book(title)

        elif chose == '5':
            print('Thank you for using my library!')
            break
        else:
            print('ridi')


if __name__ == '__main__':
    main()
