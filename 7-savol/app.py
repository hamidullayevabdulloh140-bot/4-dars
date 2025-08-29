class Library:
    def __init__(self):
        self.__books = []
    @property
    def books(self):
        return self.__books.copy()

    def add_book(self, book):
        self.__books.append(book)
        print(f"'{book}' kitobi qo‘shildi.")

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
            print(f"'{book}' kitobi o‘chirildi.")
        else:
            print(f"'{book}' topilmadi.")

l1 = Library()

l1.add_book("Python Asoslari")
l1.add_book("Sun'iy intellekt")

print("Mavjud kitoblar:", l1.books)

