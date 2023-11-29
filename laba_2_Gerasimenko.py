#1
print("Programming", "Essential", "in", sep="***", end='...')
print("Python")
#2
arrow = ["    *    ",
         "  *   *  ",
         "*       *",
         "***   ***",
         "  *   *  ",
         "  *   *  ",
         "  *****  "]
for x in arrow:
    print(x)
#3
print("I'm student")
#4
print('"I\'m"', '""learning""', '"""Python"""', sep='\n')
#5-6
number_1 = "500"
number_2 = "777"
number_1 = int(number_1, 8)
number_2 = int(number_2, 16)
print(f'number one = {number_1}, number two = {number_2}')