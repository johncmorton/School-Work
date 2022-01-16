"""
John Morton
Tic Tac Toe
"""
import time
import json
import os
from time import sleep

X = 'X'
O = 'O'
BLANK = ' '


blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    try:
        boardfile = open(filename, "r")
        board = json.loads(boardfile.read())
        return board
    except FileNotFoundError:
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    jsonboard = json.dumps(board)
    with open(filename, "w") as gamefile:
        gamefile.write(jsonboard)
        


def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    print(f" {board[0]} | {board[1]} | {board[2]} \n---+---+---\n {board[3]} | {board[4]} | {board[5]} \n---+---+---\n {board[6]} | {board[7]} | {board[8]} ")

def is_x_turn(board):
    '''Determine whose turn it is by counting the number of X's compared to O's on the board currently.'''
    if board.count("X") < board.count("O") or board.count("X") == board.count("O"):
        return True

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''

    if is_x_turn(board):
        xmove = input("X> ")
        if xmove == "q":
            save_board("Modularization Design/gameplay.json", board)
            return False
        x_intmove = int(xmove)
        board[x_intmove-1] = X
    else:
        omove = input("O> ")
        if omove == "q":
            save_board("Modularization Design/gameplay.json", board)
            return False
        o_intmove = int(omove)
        board[o_intmove-1] = O

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:\n")

board = read_board("Modularization Design/gameplay.json")

while not game_done(board):
    display_board(board)
    if play_game(board) == False:
        print("Game Saved! ")
        break
    
if game_done(board, message=False):
    display_board(board)
    game_done(board, message=True)
    if os.path.exists("Modularization Design/gameplay.json"): 
        os.remove("Modularization Design/gameplay.json")
    else:
        print("There was no saved game or this file does not exist. ")
    time.sleep(1)
    print("The game will close in 5 seconds. ")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
