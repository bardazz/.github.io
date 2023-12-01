#1
num = int(input('enter a number: '))
print(num >= 100)
#2
num1 = int(input('enter a first number: '))
num2 = int(input('enter a second number: '))
if num1 > num2:
    print(f'{num1} > {num2}')
elif num1 == num2:
    print(f'{num1} = {num2}')
else:
    print(f'{num1} < {num2}')
#3
flower = input()
if flower == 'Spathiphyllum':
    print('Yes - Spathiphyllum is the best plant ever!')
elif flower == 'spathiphyllum':
    print('No, I want a big Spathiphyllum!')
else:
    print(f'Spathiphyllum! Not {flower}!')
#4
income = float(input("Enter the annual income: "))
if income < 85528.00:
    ror = (income / 100) * 18 - 556.02
    if ror < 0:
        ror = 0
else:
    ror = (income / 100) * 32 + 14839.02
ror = round(ror, 0)
print("The tax is:", ror, "thalers")
#5
year = int(input('Введіть рік: '))

if year < 1582:
    print('Цей період не враховується.')
elif (year % 4 != 0) or ((year % 100 == 0) and (year % 400 != 0)):
    print('Це звичайний рік')
else:
    print('Це високосний рік')

#6
secret_number = 5
print(
"""
+================================+
| Welcome to my game!            |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    x = int(input('number is..?'))
    if x == secret_number:
        print('Молодець! Тепер ти вільний!')
        break
    else:
        print('Ха-ха! Ти застряг!')
#7
import time
for x in range(1, 6):
    print(f'{x} Mississippi!')
    time.sleep(1)
print('Ready or not, here I come!')
#8
while True:
    word = input('enter the word: ')

    if word == 'helicopter':
        print('You\'ve successfully left the loop.')
        break
#9
user_word = input('enter the word: ')
user_word = user_word.upper()
for letter in user_word:
    if letter in 'AEIOU':
        continue
    print(letter)
#10
user_word = input('enter the word: ')
user_word = user_word.upper()
new_word = ''
for letter in user_word:
    if letter in 'AEIOU':
        continue
    new_word += letter
print(new_word)
#11
blocks = int(input('enter the number of blocks: '))
counter = 0
while blocks > 0:
    blocks -= counter + 1
    counter += 1
    if (counter + 1) > blocks:
        break
print(counter)
#12
def hypothesis(num):
    counter = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        counter += 1
        print(int(num))
    print(f'steps = {counter}')

number = int(input('Введіть число: '))
hypothesis(number)
