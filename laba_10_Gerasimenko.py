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
        date = int(input("Введіть дату народження у форматі РікМісяцДень: "))
        date = str(date)
        if len(date) != 8:
            raise ValueError
    except:
        print('Введіть коректну дату!')
        enter_date()
    while True:
        sum = 0
        for simbol in date:
            sum += int(simbol)

        date = str(sum)

        if len(date) == 1:
            break
    print(sum)
enter_date()
#3
def input_number():
    try:
        number = int(input('Enter a number: '))
        min = int(input('Enter a min border: '))
        max = int(input('Enter a max border: '))
        if min >= max:
            raise ValueError
        check_min_max(number, min, max)
    except:
        print('Error: wrong input')
        input_number()
def check_min_max(number, min, max):
    if number > min and number < max:
        print(number)
        return
    else:
        print(f'Error: the value is not within permitted range ({min} - {max})')
        input_number()
input_number()