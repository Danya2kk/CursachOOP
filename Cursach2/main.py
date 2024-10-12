from service import *
from order import *


def print_order_details(order):
    print("Услуги в заказе:")
    for service in order.services:
        print(service)
    print("Общая стоимость:", order.total_cost)
    print("Общая продолжительность:", order.total_duration, "минут\n")


def print_service():
    print()
    print("Доступные услуги: ")
    print(f"1. Прически:\n"
          f"    {Haircut(20, 50, 'Undercut')}\n"
          f"    {Haircut(25, 60, 'Layered')}\n"
          f"2. Маникюр:\n"
          f"    {Manicure(20, 30, 'Gel')}\n"
          f"3. Массаж:\n"
          f"    {Massage(50, 60, 'Swedish')}\n"
          f"4. Педикюр:\n"
          f"    {Pedicure(25, 45, 'Classic')}\n"
          f"5. Уход за лицом:\n"
          f"    {Facial(40, 45, 'Moisturizing')}")


flag = True
menu = ("------------MENU------------\n"
        "1. Просмотр всех доступных услуг\n"
        "2. Создание заказа\n"
        "3. Просмотр информации о заказе\n"
        "4. Выход")

haircut = [Haircut(20, 50, 'Undercut'), Haircut(25, 60, 'Layered')]
manicure = [Manicure(20, 30, 'Gel')]
massage = [Massage(50, 60, 'Swedish')]
pedicure = [Pedicure(25, 45, 'Classic')]
facial = [Facial(40, 45, 'Moisturizing')]
service = [haircut, manicure, massage, pedicure, facial]
male_order = MaleOrder()
female_order = FemaleOrder()
while flag:
    print(menu)

    choice = int(input("Выберите действие: "))
    match choice:
        case 1:
            print_service()

        case 2:
            male_flag = True
            female_flag = True
            num = int(input("Введите цифру для кого делаем заказ (1 - Мужской, 2 - Женский): "))
            if num == 1:
                male_order.clear_service()
                print_service()
                print("6. Выход")
                print()
                while male_flag:
                    choice_service = int(input("Выберите услугу которую хотите добавить: "))
                    match choice_service:
                        case 1:
                            i = 1
                            for haircut in service[0]:
                                print(f"{i}. {haircut}")
                                i += 1
                            choice_style = int(input("Выберите стиль прически: "))
                            match choice_style:
                                case 1:
                                    male_order.add_service(Haircut(20, 50, 'Undercut'))
                                case 2:
                                    male_order.add_service(Haircut(25, 60, 'Layered'))
                        case 2:
                            i = 1
                            for manicure in service[1]:
                                print(f"{i}. {manicure}")
                                i += 1
                            choice_style = int(input("Выберите стиль маникюра: "))
                            match choice_style:
                                case 1:
                                    male_order.add_service(Manicure(20, 30, 'Gel'))
                        case 3:
                            i = 1
                            for massage in service[2]:
                                print(f"{i}. {massage}")
                                i += 1
                            choice_style = int(input("Выберите стиль массажа: "))
                            match choice_style:
                                case 1:
                                    male_order.add_service(Massage(50, 60, 'Swedish'))
                        case 4:
                            i = 1
                            for pedicure in service[3]:
                                print(f"{i}. {pedicure}")
                                i += 1
                            choice_style = int(input("Выберите стиль педикюра: "))
                            match choice_style:
                                case 1:
                                    male_order.add_service(Pedicure(25, 45, 'Classic'))
                        case 5:
                            i = 1
                            for facial in service[4]:
                                print(f"{i}. {facial}")
                                i += 1
                            choice_style = int(input("Выберите стиль маски для лица: "))
                            match choice_style:
                                case 1:
                                    male_order.add_service(Facial(40, 45, 'Moisturizing'))
                        case 6:
                            male_flag = False
                            print("Заказ успешно создан")

                        case _:
                            print("Неверный ввод!")
            elif num == 2:
                female_order.clear_service()
                print_service()
                print("6. Выход")
                print()
                while female_flag:

                    choice_service = int(input("Выберите услугу которую хотите добавить: "))
                    match choice_service:
                        case 1:
                            i = 1
                            for haircut in service[0]:
                                print(f"{i}. {haircut}")
                                i += 1
                            choice_style = int(input("Выберите стиль прически: "))
                            match choice_style:
                                case 1:
                                    female_order.add_service(Haircut(20, 50, 'Undercut'))
                                case 2:
                                    female_order.add_service(Haircut(25, 60, 'Layered'))
                        case 2:
                            i = 1
                            for manicure in service[1]:
                                print(f"{i}. {manicure}")
                                i += 1
                            choice_style = int(input("Выберите стиль маникюра: "))
                            match choice_style:
                                case 1:
                                    female_order.add_service(Manicure(20, 30, 'Gel'))
                        case 3:
                            i = 1
                            for massage in service[2]:
                                print(f"{i}. {massage}")
                                i += 1
                            choice_style = int(input("Выберите стиль массажа: "))
                            match choice_style:
                                case 1:
                                    female_order.add_service(Massage(50, 60, 'Swedish'))
                        case 4:
                            i = 1
                            for pedicure in service[3]:
                                print(f"{i}. {pedicure}")
                                i += 1
                            choice_style = int(input("Выберите стиль педикюра: "))
                            match choice_style:
                                case 1:
                                    female_order.add_service(Pedicure(25, 45, 'Classic'))
                        case 5:
                            i = 1
                            for facial in service[4]:
                                print(f"{i}. {facial}")
                                i += 1
                            choice_style = int(input("Выберите стиль маски для лица: "))
                            match choice_style:
                                case 1:
                                    female_order.add_service(Facial(40, 45, 'Moisturizing'))
                        case 6:
                            female_flag = False
                            print("Заказ успешно создан")

                        case _:
                            print("Неверный ввод!")
            else:
                print("Вы ввели неверную цифру")

        case 3:
            #Просмотр информации о заказе
            print()
            print("Детали мужского заказа:")
            print_order_details(male_order)

            print("Детали женского заказа:")
            print_order_details(female_order)

        case 4:
            flag = False
            print("Программа завершена!")

        case _:
            print("Неваерный ввод!")



