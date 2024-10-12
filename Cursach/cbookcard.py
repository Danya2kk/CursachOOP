class CBookCard:
    def __init__(self, author, title, publisher, year, isbn, circulation):
        self.__author = author
        self.__title = title
        self.__publisher = publisher
        self.__year = year
        self.__isbn = isbn
        self.__circulation = circulation
        self.__rating = 0

    def get_rating(self):
        return self.__rating

    def get_author(self):
        return self.__author

    def get_title(self):
        return self.__title

    def get_publisher(self):
        return self.__publisher

    def get_year(self):
        return self.__year

    def get_isbn(self):
        return self.__isbn

    def get_circulation(self):
        return self.__circulation

    def set_rating(self, rating):
        if 0 <= rating <= 10:
            self.__rating = rating
        else:
            print(f"Неверное значение рейтинга книги {self.__title}. Рейтинг может быть от 0 до 10. Значение по умолчанию 0")

    def set_author(self, author):
        self.__author = author

    def set_title(self, title):
        self.__title = title

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def set_year(self, year):
        self.__year = year

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_circulation(self, circulation):
        self.__circulation = circulation

    def __str__(self):
        return (f"Автор: {self.__author}\nЗаглавие: {self.__title}\nИздательство: {self.__publisher}\n"
                f"Год издания: {self.__year}\nISBN: {self.__isbn}\nТираж: {self.__circulation}\n"
                f"Рейтинг: {self.__rating}")

    @staticmethod
    def sort_by_year(list_books: list):
        sorted_books = sorted(list_books, key=lambda x: x.get_year())
        return sorted_books



