# ex6

class LibraryItem:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year
        self.available = True

    def check_out(self):
        if not self.available:
            print("The item is not available")
        else:
            self.available = False

    def return_item(self):
        self.available = True
        print(f"The item {self.name} is now available")


class Book(LibraryItem):
    def __init__(self, name, release_year, number_of_pages):
        super().__init__(name, release_year)
        self.number_of_pages = number_of_pages

    def info(self):
        print(
            f" Book's name: {self.name} \n Release Year: "
            f"{self.release_year} \n Number of Pages: "
            f"{self.number_of_pages} \n")


class DVD(LibraryItem):
    def __init__(self, name, release_year, length):
        super().__init__(name, release_year)
        self.length = length

    def info(self):
        print(f" DVD name: {self.name} \n Release Year: "
              f"{self.release_year} \n Length in minutes: "
              f"{self.length} \n")


class Magazine(LibraryItem):
    def __init__(self, name, release_year, edition):
        super().__init__(name, release_year)
        self.edition = edition

    def info(self):
        print(f" Magazine's name: {self.name} \n Release Year: "
              f"{self.release_year} \n Edition: "
              f"{self.edition} \n")


book = Book("Book1", 2010, 484)
book.info()
dvd = DVD("DVD1", 2015, 128)
dvd.info()
magazine = Magazine("Magazine1", 2020, "edition1")
magazine.info()

book.check_out()
book.check_out()
book.return_item()
