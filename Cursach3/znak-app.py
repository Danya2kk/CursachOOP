import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import re
from znak import *


class ZNAKApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Управление данными ЗНАК")
        self.people = []

        # Меню
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Загрузить", command=self.load_data)
        file_menu.add_command(label="Сохранить", command=self.save_data)

        # Элементы GUI
        self.listbox = tk.Listbox(root, width=100, height=15)
        self.listbox.pack(pady=20)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Добавить", command=self.add_person_window).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Удалить", command=self.remove_person).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Поиск по месяцу", command=self.search_by_month).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Сортировка", command=self.add_sort_info).pack(side=tk.LEFT, padx=10)

        self.refresh_listbox()

    def add_sort_info(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Выбор сортировки")

        tk.Button(add_window, text="Сортировка по фамилии", command=lambda: self.sort_data('фамилия')).grid(row=0, columnspan=2, pady=10)
        tk.Button(add_window, text="Сортировка по имени", command=lambda: self.sort_data('имя')).grid(row=1, columnspan=2, pady=10)
        tk.Button(add_window, text="Сортировка по знаку зодиака", command=lambda: self.sort_data('знак зодиака')).grid(row=2, columnspan=2, pady=10)
        tk.Button(add_window, text="Сортировка по дате", command=lambda: self.sort_data('дата рождения')).grid(row=3, columnspan=2, pady=10)

    def add_person_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Добавить человека")

        tk.Label(add_window, text="Фамилия:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.surname_entry = tk.Entry(add_window)
        self.surname_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Имя:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(add_window)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Знак Зодиака:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.zodiac_entry = tk.Entry(add_window)
        self.zodiac_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_window, text="Дата Рождения (дд.мм.гггг):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.birth_date_entry = tk.Entry(add_window)
        self.birth_date_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(add_window, text="Добавить", command=self.add_person).grid(row=4, columnspan=2, pady=10)

    def add_person(self):
        if self.validate_data():
            surname = self.surname_entry.get().strip().capitalize()
            name = self.name_entry.get().strip().capitalize()
            zodiac_sign = self.zodiac_entry.get().strip().capitalize()
            birth_date = list(map(int, self.birth_date_entry.get().strip().split('.')))
            new_person = ZNAK(surname, name, zodiac_sign, birth_date)
            self.people.append(new_person)
            self.sort_data('знак зодиака')
            self.refresh_listbox()
            self.clear_fields()
            messagebox.showinfo("Успешно", "Человек успешно добавлен!")

    def clear_fields(self):
        self.surname_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.zodiac_entry.delete(0, tk.END)
        self.birth_date_entry.delete(0, tk.END)

    def remove_person(self):
        selected = self.listbox.curselection()
        if selected:
            self.people.pop(selected[0])
            self.refresh_listbox()

    def search_by_month(self):
        month = simpledialog.askinteger("Поиск", "Введите месяц (число от 1 до 12):")
        if month:
            found = [person for person in self.people if person.get_birth_date()[1] == month]
            if found:
                messagebox.showinfo("Результаты поиска", "\n".join(str(person) for person in found))
            else:
                messagebox.showinfo("Результаты поиска", "Нет данных по заданному месяцу.")

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for person in self.people:
            self.listbox.insert(tk.END, str(person))

    def load_data(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "r") as f:
                for line in f:
                    data = line.strip().split(',')
                    surname = data[0]
                    name = data[1]
                    zodiac_sign = data[2]
                    birth_date = list(map(int, data[3].split('.')))
                    new_person = ZNAK(surname, name, zodiac_sign, birth_date)
                    self.people.append(new_person)
                self.refresh_listbox()
            messagebox.showinfo("Успешно", f"Данные загружены из файла: {filename}")

    def save_data(self):
        filename = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "w") as f:
                for person in self.people:
                    f.write(
                        f"{person.get_surname()},{person.get_name()},{person.get_zodiac_sign()},{person.get_birth_date()[0]}.{person.get_birth_date()[1]}.{person.get_birth_date()[2]}\n")
            messagebox.showinfo("Успешно", f"Данные сохранены в файл: {filename}")

    def sort_data(self, sort_option):
        if sort_option:
            if sort_option.lower() == 'фамилия':
                self.people.sort(key=lambda x: x.get_surname())
            elif sort_option.lower() == 'имя':
                self.people.sort(key=lambda x: x.get_name())
            elif sort_option.lower() == 'знак зодиака':
                self.people.sort(key=lambda x: x.get_zodiac_sign())
            elif sort_option.lower() == 'дата рождения':
                self.people.sort(key=lambda x: (x.get_birth_date()[2], x.get_birth_date()[1], x.get_birth_date()[0]))
            self.refresh_listbox()

    def validate_data(self):
        surname = self.surname_entry.get().strip()
        name = self.name_entry.get().strip()
        zodiac_sign = self.zodiac_entry.get().strip()
        birth_date = self.birth_date_entry.get().strip()

        if not surname or not name or not zodiac_sign or not birth_date:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
            return False

        name_pattern = r'^[A-ZА-Я].*$'
        if not re.match(name_pattern, surname):
            messagebox.showerror("Ошибка", "Пожалуйста, введите фамилию с большой буквы.")
            self.surname_entry.delete(0, tk.END)
            return False

        if not re.match(name_pattern, name):
            messagebox.showerror("Ошибка", "Пожалуйста, введите имя с большой буквы.")
            self.name_entry.delete(0, tk.END)
            return False

        if not re.match(name_pattern, zodiac_sign):
            messagebox.showerror("Ошибка", "Пожалуйста, введите знак зодиака с большой буквы.")
            self.zodiac_entry.delete(0, tk.END)
            return False

        date_pattern = r'^\d{2}\.\d{2}\.\d{4}$'
        if not re.match(date_pattern, birth_date):
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректную дату (дд.мм.гггг).")
            self.birth_date_entry.delete(0, tk.END)
            return False

        day, month, year = map(int, birth_date.split('.'))
        if not (1 <= month <= 12):
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректный месяц (число от 1 до 12).")
            self.birth_date_entry.delete(0, tk.END)
            return False

        if month in [4, 6, 9, 11] and day > 30:
            messagebox.showerror("Ошибка",
                                 "Пожалуйста, введите корректный день для выбранного месяца (диапазон от 1 до 30).")
            self.birth_date_entry.delete(0, tk.END)
            return False
        elif month == 2:
            leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            if leap_year and day > 29:
                messagebox.showerror("Ошибка",
                                     "Пожалуйста, введите корректный день для выбранного месяца (диапазон от 1 до 29).")
                self.birth_date_entry.delete(0, tk.END)
                return False
            elif not leap_year and day > 28:
                messagebox.showerror("Ошибка",
                                     "Пожалуйста, введите корректный день для выбранного месяца (диапазон от 1 до 28).")
                self.birth_date_entry.delete(0, tk.END)
                return False
        elif day < 1 or day > 31:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректный день (диапазон от 1 до 31).")
            self.birth_date_entry.delete(0, tk.END)
            return False

        return True


if __name__ == "__main__":
    root = tk.Tk()
    app = ZNAKApp(root)
    root.mainloop()



