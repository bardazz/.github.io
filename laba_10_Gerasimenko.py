#1
string1 = 'qwe'
string2 = 'zxc'
string3 = ''
for x in string1:
    index = string2.find(x)
    string3 += string2[index]
if string1 == string3:
    print('Yes!')
else:
    print('Nope!')
#2
def enter_date():
    try:
        date = input("Введіть дату народження в форматі РікМісяцДень: ")
        if len(date) != 8 or not date.isdigit():
            raise ValueError
    except ValueError:
        print('Введіть коректну дату!')
        enter_date()
    while True:
        total = sum(int(simbol) for simbol in date)
        date = str(total)

        if len(date) == 1:
            break
    print(total)
enter_date()
#3
def input_number():
    try:
        number = int(input('Enter a number: '))
        min_val = int(input('Enter a min border: '))
        max_val = int(input('Enter a max border: '))
        if min_val >= max_val:
            raise ValueError
        check_min_max(number, min_val, max_val)
    except ValueError:
        print('Помилка: неправильне введення')
        input_number()

def check_min_max(number, min_val, max_val):
    if min_val < number < max_val:
        print(number)
    else:
        print(f'Некоректне значення({min_val} - {max_val})')
        input_number()
input_number()
