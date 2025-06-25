def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_win(board, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_draw(board):
    return all(space != ' ' for space in board)

def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid position. Choose a number between 1 and 9.")
                continue
            if board[move] != ' ':
                print("That spot is already taken. Choose another one.")
                continue
            board[move] = current_player
            print_board(board)

            if check_win(board, current_player):
                print(f"Player {current_player} wins! 🎉")
                break
            if is_draw(board):
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        except ValueError:
            print("Please enter a valid number.")

tic_tac_toe()

