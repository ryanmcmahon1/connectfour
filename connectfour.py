import numpy as np
from player import Player

ROWS, COLS = 6, 7
board = 0

# moves piece for current player into requested location
def move(board, piece):

    col = 0
    row = 0

    valid = False
    while (not valid):
        # get user input to place this player's piece
        print("Enter the column you want to put your piece in")
        col = int(input())

        # determining which row this piece should go into
        row = calc_row(board, col)
        if (row != -1):
            valid = True
            board[row][col] = piece
        else:
            print("row is full, enter another row")

    # print the new state of the board
    print(board)
    return row, col

# calculates row this piece should be placed in (-1 if error)
def calc_row(board, col):

    # getting column and searching for where we can place the piece
    col = [row[col] for row in board]

    if (col[-1] == 0):
        return len(col) - 1
    else:
        return np.min(np.nonzero(col)) - 1

# checks if an array has four instances of a value in a row
def check_four(arr, value):
    count = 0
    for i in np.arange(len(arr)):
        if (arr[i] == value):
            count = count + 1
            if (count == 4):
                return True
        else:
            count = 0
    
    return False

# checks horizontal axis for a win
def horizontal(board, piece, row_num):
    row = board[row_num]
    return check_four(row, piece)    

# checks vertical axis for a win
def vertical(board, piece, col_num):
    col = [row[col_num] for row in board]
    return check_four(col, piece)

# # checks diagonal axis for a win
def diagonal(board, piece, row, col):
    diagonal1 = np.diagonal(board, col - row)
    diagonal2 = np.fliplr(board).diagonal(COLS - 1 - col - row)
    return check_four(diagonal1, piece) or check_four(diagonal2, piece)

# checks if this player has won after this move
def check_win(board, piece, row, col):
    return horizontal(board, piece, row) or vertical(board, piece, col) or diagonal(board, piece, row, col)

# checks if there are no available moves for this game, which means we have a tie
def check_tie(board):
    row = board[0]
    if (row.nonzero()[0].size == COLS):
        return True
    return False

# runs one turn for the specified player
def run_turn(board, player):
    print(player.name + "'s turn")
    row, col = move(board, player.get_piece())
    if (check_win(board, player.get_piece(), row, col)):
        print(player.name, "wins")
        return player.get_piece()
    if (check_tie(board)):
        print("Tie! you guys suck")
        return 0
    return -1

# function that runs one game
def play_game(player1, player2):

    # initialize the board
    board = np.zeros((ROWS, COLS), dtype=int)
    print(board)

    # each player has 1 move
    while (1):
        status = run_turn(board, player1)
        if (status != -1):
            return status
        status = run_turn(board, player2)
        if (status != -1):
            return status

# prints current score for this player
def print_score(player):
    print(player.get_name(), "has", player.get_score(), "wins")

# function that runs several games in a row
def play_match():
    # assigning each player a piece number and name
    print("Enter player 1's name:")
    name1 = str(input())
    print("Enter player 2's name:")
    name2 = str(input())
    player1 = Player(name1, 1, 0)
    player2 = Player(name2, 2, 0)

    while (1):
        # running one game, then increasing the score of each player
        result = play_game(player1, player2)
        if (result == 1):
            player1.set_score(player1.get_score() + 1)
        if (result == 2):
            player2.set_score(player2.get_score() + 1)

        # displaying current score
        print("Current score:")
        print_score(player1)
        print_score(player2)
        
        print("Play more rounds? (Y/N)")
        response = str(input())
        if (response == "Y"):
            play_game(player1, player2)
        else:
            print("bye bye!")
            return 

# function that runs several games
play_match()