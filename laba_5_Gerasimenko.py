#1
hot_list = [1, 2, 3, 4, 5]
hot_list[2] = int(input('enter the number: '))
hot_list.pop()
print(len(hot_list))
print(hot_list)
#2
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

user_input = input('Введіть числа, розділені пробілами: ')
user_list = list(map(int, user_input.split()))  
sorted_list = bubble_sort(user_list.copy()) 
print(f'Відсортований список: {sorted_list}')
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_set = set(my_list)  
print(f'Список з унікальними елементами: {my_set}')
chess_board = [['_' for _ in range(8)] for _ in range(8)]
positions = [(0, 0), (0, 7), (7, 0), (7, 7)] 
for row, col in positions:#Peremena
    chess_board[row][col] = 'T'#PozT
for row in chess_board:
    print(' '.join(row))
