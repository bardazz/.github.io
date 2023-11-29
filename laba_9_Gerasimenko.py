text = input("Enter your message: ")
def enter_number():
    try:
        num = int(input('Enter a number (1-25): '))
        if num > 25 or num < 1:
            raise ValueError
    except:
        print('Please enter a number between 1 and 25!')
        enter_number()

    cipher = ''

    for char in text:

        if not char.isalpha():
            cipher += char
        else:
            x_char = char.upper()
            code = ord(x_char) + num

            if code > 90:
                code = 64 + (code - 90)

            if char.isupper():
                cipher += chr(code).upper()
            elif char.islower():
                cipher += chr(code).lower()

    print(f'Cipher: {cipher}')
enter_number()