#1
n = int(input("n?: "))
numbers = (2, 7, 1, 8, 5, 9, 3, 6, 4)
result = [q for q in numbers if q < n]
print(result)
#2
my_tuple = ('one', 'two', 'three')
print(', '.join(my_tuple))
#3
library = {
    'Book1': {'Автор': 'Автор1', 'Рік видання': 2017, 'Кількість сторінок': 368},
    'Book2': {'Автор': 'Автор2', 'Рік видання': 2005, 'Кількість сторінок': 224},
    'Book3': {'Автор': 'Автор3', 'Рік видання': 2023, 'Кількість сторінок': 483},
}
book_title = input("введіть назву книги: ")
if book_title in library:
    print(f"\nІнформація про книгу '{book_title}':")
    for key, value in library[book_title].items():
        print(f"{key}: {value}")
else:
    print(f"\nКниги з назвою '{book_title}' немає в бібліотеці.")
#4
students = {
    'Гордієнко': ('Олександр', 29, 'Інформатика'),
    'Герасименко': ('Влад', 20, 'Екологія'),
    'Сизченко': ('Іван', 20, 'Друід'),
}
student_lastname = input("Введіть прізвище студента: ")
if student_lastname in students:
    print(f"\nІнформація про студента {student_lastname}:")
    print(f"Ім'я: {students[student_lastname][0]}")
    print(f"Вік: {students[student_lastname][1]}")
    print(f"Спеціальність: {students[student_lastname][2]}")
else:
    print(f"\nСтудента із прізвищем '{student_lastname}' немає в словнику.")
#5
def add_phone_number(contacts, contact_name, new_phone_number):
    if contact_name in contacts:
        contacts[contact_name].append(new_phone_number)
        print(f"Новий номер телефону {new_phone_number} доданий для контакту {contact_name}.")
    else:
        print(f"Контакту {contact_name} немає в телефонній книзі.")
phone_book = {
    'Гордієнко': ['+380-298-126-12-90', '+380-965-421-34-22'],
    'Герасименко': ['+380-853-342-87-24' '+380-632-34-22-11'],
    'Сизченко': ['+380-888-553-55-12'],
}
add_phone_number(phone_book, input('Введіть ім\'я: '), input('Введіть номер: '))
print("\nСписок номерів телефонів для всіх контактів:")
for contact, phone_numbers in phone_book.items():
    print(f"{contact}: {phone_numbers}")