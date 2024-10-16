# Initialize the game board
board = [' ' for _ in range(9)]

# Display the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Check for a winner
def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]             # diagonals

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check for a tie
def check_tie():
    return ' ' not in board

# Player makes a move
def make_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move >= 0 and move < 9 and board[move] == ' ':
                board[move] = player
                break
            else:
                print("Invalid move! Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Game loop
def play_game():
    current_player = 'X'
    
    while True:
        print_board()
        make_move(current_player)
        
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif check_tie():
            print_board()
            print("It's a tie!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
