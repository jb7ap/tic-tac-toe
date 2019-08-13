import time
from collections import defaultdict
import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
wins = [[0,1,2],[3,4,5],[6,7,8],[2,5,8],[1,4,7],[0,3,6],[0,4,8],[2,4,6]]

def drawBoard(board):
    print()
    print('     |       |      ')
    print('  ' + board[0] + '  ' + '|' + '   ' + board[1] + '   ' + '|' + '  ' + board[2] + '  ')
    print('     |       |      ')
    print("--------------------")
    print('     |       |      ')
    print('  ' + board[3] + '  ' + '|' + '   ' + board[4] + '   ' + '|' + '  ' + board[5] + '  ')
    print('     |       |      ')
    print("--------------------")
    print('     |       |      ')
    print('  ' + board[6] + '  ' + '|' + '   ' + board[7] + '   ' + '|' + '  ' + board[8] + '  ')
    print('     |       |      ')

def checkIfWon(board):
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        print("You won!")
        exit()
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        print("You won!")
        exit()
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        print("You won!")
        exit()
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        print("You won!")
        exit()
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        print("You won!")
        exit()
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        print("You won!")
        exit()
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        print("You won!")
        exit()
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        print("You won!")
        exit()

def checkIfLost(board):
    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        print("You lost!")
        exit()
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        print("You lost!")
        exit()
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        print("You lost!")
        exit()
    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        print("You lost!")
        exit()
    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
        print("You lost!")
        exit()
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        print("You lost!")
        exit()
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        print("You lost!")
        exit()
    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        print("You lost!")
        exit()

def comp_algorithm(board):
    x_count = 0
    o_count = 0
    corners = []
    possible_comb =[]
    x_list = []
    o_list = []
    empty = []
    next_space = []

    for combinations in wins:
        for position in combinations:
            if board[position] == 'X':
                x_count = x_count + 1
            elif board[position] == 'O':
                o_count = o_count + 1
        x_list.append(x_count)
        o_list.append(o_count)
        x_count = 0
        o_count = 0

    if board[4] == " ":
        next_space.append(4)

    d = defaultdict(list)
    for index, e in enumerate(o_list):
        d[e].append(index)
    o_two_list = (d[2])

    for x in o_two_list:
        possible_comb.append(wins[x])
    for combinations in possible_comb:
        for position in combinations:
            if board[position] == " ":
                next_space.append(position)

    indices = [i for i, x in enumerate(board) if x == " "]
    empty.append(indices)

    d = defaultdict(list)
    for index, e in enumerate(x_list):
        d[e].append(index)
    two_list = (d[2])

    for x in two_list:
        possible_comb.append(wins[x])
    for combinations in possible_comb:
        for position in combinations:
            if board[position] == " ":
                next_space.append(position)

    if len(next_space) != 0:
        a = next_space[0]
        board[a] = "O"
        next_space.remove(a)
    else:
        board[(random.choice(random.choice(empty)))] = "O"
drawBoard(board)

while ' ' in board:
    while True:
        try:
            pos = int(input("Choose a spot (1-9): "))
            while pos == 0:
                print("Please enter a number between 1 and 9")
                pos = int(input("Choose a spot"))
            if board[pos-1] != ' ':
                print("Spot is already taken")
            else:
                board[pos-1] = 'X'
                drawBoard(board)
                checkIfWon(board)
                comp_algorithm(board)
                time.sleep(1)
                drawBoard(board)
                checkIfLost(board)
                break
        except (ValueError, IndexError):
            if ' ' in board:
                print("Please enter a number between 1 and 9")
            else:
                print("It's a draw")
                exit()
drawBoard(board)


