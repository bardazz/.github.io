import math
#1
def g_function(x, zero, two):
    exp = -((x - zero) ** 2) / (2 * two ** 2)
    cf = 1 / (math.sqrt(2 * math.pi) * two)
    res = cf * math.exp(exp)
    return res
zero = 0
two = 1
x = input("Введіть значення 'X': ")
g_value = g_function(float(x), zero, two)
print(f'Значення функції Гауса для X = {x}: {g_value}')
#2
john = 3
mary = 5
adam = 6
totalApples = john + mary + adam
print(john, mary, adam, sep=', ')
print(f'Загальна к-сть яблук: {totalApples}')
#3
km = 12.25
mil = 7.38

mil_to_km = mil * 1.61
km_to_mil = km / 1.61

print(mil, "Милі це", round(mil_to_km, 2), "Кілометр")
print(km, "Кілометра це", round(km_to_mil, 2), "милі")
#4
x = input()
x = float(x)
y = ((x ** 3) * 3) - ((x ** 2) * 2) + (3 ** x) - 1
print("y =", y)
#5
hours = 2 
seconds = 3600
print("Hours: ", hours) 
#6
a = float(input('Введіть перше число: '))
b = float(input('Введіть друге число: '))
print(f'Результат додавання {a} + {b} = {a + b}')
print(f'Результат віднімання {a} - {b} = {a - b}')
print(f'Результат множення {a} * {b} = {a * b}')
if (b == 0):
    print(f'Вибачте, на нуль ділити неможливо!')
else:
    print(f'Результат ділення {a} / {b} = {a / b}')

print("\nЦе все!")
#7
x = float(input("Enter value for x: "))
y = 1 / (x + 1 / (x + 1 / (x + 1 / (x + (1 / x)))))
print("y =", y)
#8
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
bor = int(input("Event duration (minutes): "))
def func_time(hour, mins, bor):
    if (mins + bor < 60):
        mins += bor
        return print(f'{hour}:{mins}') if mins > 9 else print(f'{hour}:0{mins}')
    else:
        hour += 1
        mins -= 60
        if hour > 23:
             hour -= 24
        func_time(hour, mins, bor)
func_time(hour, mins, bor)
