library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(book):
    if not book in library:
        library.append(book)
    else:
        print('Book is already in library')

add_book(("2020", "Amilcar Cornier"))
print(library)
