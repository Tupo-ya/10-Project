import random

def draw_board(elem: list):
    if len(elem) != 9:
        print('Список элементов неверный!')
        input()

    for i in range(3):
        print(" " + elem[i*3] + " | " + elem[i*3+1] + " | " + elem[i*3+2])
        if i != 2:
            print("---+---+---")


draw_board(['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'])