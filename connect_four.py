"""
Planning:
    Setup: Initialize the game board with empty spaces.
    Game Loop:
        - Display the current state of the board.
        - Prompt the current player for their move.
        - Validate the move and update the board.
        - Check for a win or draw condition.
        - Switch players and repeat the loop.
    Winning Condition:
        - Check for four consecutive tokens in a row, column, or diagonal.
        - If a winning condition is met, end the game and declare the winner.
    Draw Condition:
        - If the board is full and no winning condition is met, end the game as a draw.
    User Input:
        - Accept user input for column selection.
        - Validate the input to ensure it's within the bounds of the board and the column is not full.
    Display:
        - Display the current state of the board after each move.
        - Use ASCII characters to represent the game board and player tokens.
    Player Switching:
        - Toggle between players after each move.
    Game Over Message:
        - Display a message indicating the winner or a draw when the game ends.
"""
import sys
import random
import keyboard
import time

# Initial game board - 7x6 grid with empty cells:
board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

def connect_four():
    """Start the game"""
    print("Welcome to Connect Four")
    print("Press ENTER to start the game or ESC to exit")
    
    while True:
        key_pressed = keyboard.read_event(suppress=True).name
        if key_pressed == 'enter':
            print("Starting the game...")
            time.sleep(2)
            print("Game started!\n")
            break
        elif key_pressed == 'esc':
            print("Exiting the game...")
            sys.exit()
    
    # Prompt users to enter their names
    player_1 = input("Player 1 name: ")
    while not player_1:
        player_1 = input("Please enter a valid name for Player 1: ")
    
    player_2 = input("Player 2 name: ")
    while not player_2:
        player_2 = input("Please enter a valid name for Player 2: ")
    
    # Determine who plays first
    print("Let's roll the dice to see which player will go first.")
    keyboard.wait('enter')
    number_player_1 = random.randint(1, 6)
    number_player_2 = random.randint(1, 6)
    while number_player_1 == number_player_2:
        number_player_1 = random.randint(1, 6)
        number_player_2 = random.randint(1, 6)
    
    print(f"{player_1} rolls: {number_player_1}")
    print(f"{player_2} rolls: {number_player_2}")
    
    current_player = player_1 if number_player_1 > number_player_2 else player_2
    print(f"{current_player} will start first.\n")
    display_board(board)

def display_board(board):
    """Display the current state of the game board."""
    print('  0   1   2   3   4   5   6   \n')
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print()
        print("+---" * len(row) + "+")

def toggle_player(current_player, player_1, player_2):
    """Toggle between the first and second player"""
    return player_2 if current_player == player_1 else player_1

def validating_player_move(input):
    """Check if the selected column is valid / not full and if the move is legal"""
    legal_inputs = [0, 1, 2, 3, 4 ,5 ,6]
    if input.isdigit():  # Check if input is a digit
        column = int(input)
        if column in legal_inputs:
            for i in range(len(board)):
                if board[i][column] == ' ':
                    return True
    return False

def execute_player_move(valid_input):
    """Execute the player's move and update the board"""
    for i in range(len(board) - 1, -1, -1):
        column = int(valid_input)
        if board[i][column] == ' ':
            board[i][column] = 'X'
            break

def check_for_winner():
    """Check if there's a winner on the current board."""
    # Check rows:
    
    # Check columns:
    
    # Check diagonals (top-left to bottom-right):

    # Check diagonals (bottom-left to top-right):

connect_four()

# player_input = input('shoose column between 0 to 6: ')
while not validating_player_move(player_input):
    player_input = input('Please, shoose column between 0 to 6: ')



# display_board(board)