import random

# Game Board
board = [' ' for _ in range(9)]

# Function to draw the game board
def draw_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Function to handle player move
def player_move():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

# Function to handle AI move using Minimax algorithm
def ai_move():
    best_score = float('-inf')
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    insert_letter('O', best_move + 1)

# Minimax function
def minimax(board, depth, is_maximizing):
    if check_winner() == 'X':
        return -10 + depth
    elif check_winner() == 'O':
        return 10 - depth
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Function to check if a space is free
def space_is_free(pos):
    return board[pos - 1] == ' '

# Function to insert a letter in the board
def insert_letter(letter, pos):
    board[pos - 1] = letter

# Function to check if the board is full
def check_draw():
    return ' ' not in board

# Function to check for a winner
def check_winner():
    winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    return None

# Main game loop
def play_game():
    print('Welcome to Tic Tac Toe!')
    draw_board()
    while True:
        player_move()
        draw_board()
        if check_winner() == 'X':
            print('Congratulations, you won!')
            break
        elif check_draw():
            print('It\'s a draw!')
            break
        ai_move()
        draw_board()
        if check_winner() == 'O':
            print('Sorry, the AI won!')
            break

play_game()