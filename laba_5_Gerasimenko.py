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
bubble_sort(input())
print(f'Відсортований список: {bubble_sort}')
#3
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list = set(my_list)
print(f'The list with unique elements only: {my_list}')
#4
chess_board = [['_' for _ in range(8)] for _ in range(8)]
chess_board[0][0] = 'T'
chess_board[0][8 - 1] = 'T'
chess_board[8 - 1][0] = 'T'
chess_board[8 - 1][8 - 1] = 'T'
for row in chess_board:
    print(' '.join(row))