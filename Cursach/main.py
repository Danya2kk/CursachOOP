from cbookcard import CBookCard
import re


def is_valid_isbn(isbn: str):
    pattern = r"\d{3}\-\d{3}\-\d{1}"

    if re.match(pattern, isbn):
        return True
    else:
        return False


flag = True
menu = ("-----------------MENU-----------------\n"
        "1. Добавить информацию о книге\n"
        "2. Запуск программы с исходными данными\n"
        "3. Просмотр всех книг\n"
        "4. Сортировка по году издания\n"
        "5. Удалить все книги\n"
        "6. Выход\n")

sep = "------------------------------------------"
books = []
while flag:
    print(menu)
    choice = int(input("Выберите действие: "))

    match choice:
        case 1:
            num = int(input("Введите количестсво книг: "))

            for i in range(num):
                author = input("Введите автора книги: ")
                title = input("Введите название книги: ")
                publisher = input("Введите публикатора: ")
                year = int(input("Введите год написания книги: "))
                while True:
                    isbn = input("Введите ISBN(xxx-xxx-x): ")
                    if is_valid_isbn(isbn):
                        break
                    else:
                        print("ISBN введнен неверно. Пожалуйста, введите в формате xxx-xxx-x")

                circulation = int(input("Введите тираж: "))

                book = CBookCard(author, title, publisher, year, isbn, circulation)

                rating = int(input("Введите рейтинг: "))
                book.set_rating(rating)
                books.append(book)
                print("Книга добавлена!")
        case 2:
            book1 = CBookCard("Лев Толстой", "Война и мир", "Русский вестник", 1869, "821-161-1", 5000)
            book1.set_rating(10)

            book2 = CBookCard("Федор Достоевский", "Преступление и наказание", "Русский вестник", 1866, "821-161-1",
                              3000)
            book2.set_rating(9)

            book3 = CBookCard("Иван Тургенев", "Муму", "Русский вестник", 1852, "342-564-2", 6000)
            book3.set_rating(5)

            books = [book1, book2, book3]
            print("Исходные данные успешно загружены")

        case 3:
            if books:
                for book in books:
                    print(sep)
                    print(book)
            else:
                print("В библиотеке нет книг!")

        case 4:
            print("-----Список книг до сортировки-----")
            for book in books:
                print(sep)
                print(book)

            print("-----Список книг после сортировки по году-----")
            sort = CBookCard.sort_by_year(books)
            for book in sort:
                print(sep)
                print(book)

        case 5:
            if len(books) == 0:
                print("В библиотеке нет книг!")

            else:

                books.clear()
                print("Все книги удалены")

        case 6:
            flag = False
            print("Программа успешно завершена!")

        case _:
            print("Неверный ввод!")



