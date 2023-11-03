
# ! Для работы этой программы нужно установить colorama 
# pip install colorama

import random
import os
from colorama import init, Fore, Style
init()

# ? Это, чтобы автоматически перезапускать игру
auto_restart = True

def hello() -> None:
    print('Хелло ин ве гаме Крестики-Нолики!')
    print('Вот так надо вписывать свой ход:')
    skip = False
    for i in range(1, 10):
        if i % 3 == 0:
            skip = True
        else:
            skip = False
        print(f'{i}', end='\n' if skip else ' ')
    print('\n')

def get_active_cell(board: list) -> int:
    result = 0
    for i in board:
        if not i.isdigit():
            result += 1
    
    return result

def draw_board(board: list) -> None:    
    format_board = []
    # ? Чтобы сетка не рушилась в клетках, в которых ничего нет прибавляем пробел
    for i in range(len(board)):
        format_board.append(board[i] if board[i] != '' else ' ')

    # ? Тут рисуем сетку
    for i in range(3):
        cell_1 = format_board[i*3]
        cell_2 = format_board[i*3+1]
        cell_3 = format_board[i*3+2]

        if cell_1 == 'X':
            cell_1 = f"{Fore.GREEN}{cell_1}{Style.RESET_ALL}"
        elif cell_1 == 'O':
            cell_1 = f"{Fore.YELLOW}{cell_1}{Style.RESET_ALL}"

        if cell_2 == 'X':
            cell_2 = f"{Fore.GREEN}{cell_2}{Style.RESET_ALL}"
        elif cell_2 == 'O':
            cell_2 = f"{Fore.YELLOW}{cell_2}{Style.RESET_ALL}"

        if cell_3 == 'X':
            cell_3 = f"{Fore.GREEN}{cell_3}{Style.RESET_ALL}"
        elif cell_3 == 'O':
            cell_3 = f"{Fore.YELLOW}{cell_3}{Style.RESET_ALL}"

        print(" " + cell_1 + " | " + cell_2 + " | " + cell_3)

        if i != 2:
            print("---+---+---")

def set_cell(board: list, index: int, sim: str) -> list:
    board[index] = sim
    return board

def get_player_move(board: list, player: str) -> list:
    while True:
        pos = int(input('Введите номер клетки: '))-1
        if pos > 8 or pos < 0 or not board[pos].isdigit():
            print('Неверный ввод!')
        else:
            break
    
    return set_cell(board, pos, player)


def get_computer_move(board: list, player: str) -> list:
    if get_active_cell(board) == 9:
        return board
    while True:
        pos = random.randint(0, 8)
        if board[pos].isdigit():
            break
    
    return set_cell(board, pos, player)


def check_win(board: list, player_sim: str) -> bool:
    win_combo = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combo:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player_sim:
            return True
    
    return False

def main():
    hello()
    
    print('За кого будете играть?')
    print('1 - X')
    print('2 - O')
    player_sim = 'X' if int(input('Введите символ для игры: ')) == 1 else 'O'
    pc_sim = 'X' if player_sim == 'O' else 'O'

    global_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    while True:
        os.system('cls')
        
        draw_board(global_board)

        if check_win(global_board, player_sim):
            print('Вы победили!')
            break

        if check_win(global_board, pc_sim):
            print('Компьютер победил!')
            break

        if get_active_cell(global_board) == 9:
            print('Ничья!')
            break

        global_board = get_player_move(global_board, player_sim)
        global_board = get_computer_move(global_board, pc_sim)
            

if __name__ == '__main__':
    while auto_restart:
        main()
        input()
    