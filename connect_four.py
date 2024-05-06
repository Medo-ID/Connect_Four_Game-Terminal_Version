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


# Initial game board - 7x6 grid with empty cells:
board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def __repr__(self):
        return f"My name is {self.name}, my symbol is {self.symbol}"

def connect_four(player1, player2):
    """Start the game"""
    # Determine who plays first
    number_player1 = random.randint(1, 6)
    number_player2 = random.randint(1, 6)
    while number_player1 == number_player2:
        number_player1 = random.randint(1, 6)
        number_player2 = random.randint(1, 6)
    
    print(f"{player1.name} rolls: {number_player1}")
    print(f"{player2.name} rolls: {number_player2}")
    
    current_player = player1 if number_player1 > number_player2 else player2
    print(f"{current_player.name} will start first.\n")
    
    # while no winner or no draw:
    while not check_for_winner():
        # display current board
        display_board()
        
        # prompt player to make move
        
        current_player_input = input(f'{current_player.name} - Choose between 0 to 6 to make a move: ')
        while not validating_player_move(current_player_input):
            current_player_input = input(f'{current_player.name} - Please, Make sure you are following the rules. Choose between 0 to 6 to make a move: ')
        
        # execute the move
        execute_player_move(current_player_input, current_player.symbol)
        
        # check for winner
        if check_for_winner():
            display_board()
            game_state = 'game_over'
            print(f'Game Over! - Game result: {current_player.name} is the winner!')
            break
        
        # check for draw
        if check_for_draw():
            display_board()
            game_state = 'draw'
            print(f"Game Over! - Game result: Tie!")
            break
        
        # switch player
        current_player = toggle_player(current_player, player1, player2)
    
    if game_state == 'game_over':
        print('exiting the game...')
        
        sys.exit()
    elif game_state == 'draw':
        print("Press ENTER to start new game or ESC to exit")
        while True:
            key_pressed = keyboard.read_event(suppress=True).name
            if key_pressed == 'enter':
                print("Starting new game...")
                # Reset the board to an empty state for a new game
                global board  # Declare board as global to modify it within the function
                board = [
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ']
                ]
                print("Game started!\n")
                break
            elif key_pressed == 'esc':
                print("Exiting the game...")
                sys.exit()
        connect_four(player1, player2)

def display_board():
    """Display the current state of the game board."""
    print('  0   1   2   3   4   5   6   \n')
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print()
        print("+---" * len(row) + "+")

def validating_player_move(input):
    """Check if the selected column is valid / not full and if the move is legal"""
    legal_inputs = [0, 1, 2, 3, 4 ,5 ,6]
    if input.isdigit():  # Check if input is a digit
        col = int(input)
        if col in legal_inputs:
            for row in range(len(board)):
                if board[row][col] == ' ':
                    return True
    return False

def execute_player_move(valid_input, symbol):
    """Execute the player's move and update the board"""
    for row in range(len(board) - 1, -1, -1):
        col = int(valid_input)
        if board[row][col] == ' ':
            board[row][col] = symbol
            break

def check_for_winner():
    """Check if there's a winner on the current board. return thewinning symbol. else return None"""
    # Check rows:
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            sequence = board[row][col:col + 4]  # Get a sequence of 4 symbols
            if all(symbol == sequence[0] and symbol != ' ' for symbol in sequence):
                return sequence[0]
    
    # Check columns: (similar logic as rows)
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            sequence = [board[i][col] for i in range(row, row + 4)]
            if all(symbol == sequence[0] and symbol != ' ' for symbol in sequence):
                return sequence[0]
    
    # Check diagonals (top-left to bottom-right): (similar logic as rows)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            sequence = [board[row + i][col + i] for i in range(4)]
            if all(symbol == sequence[0] and symbol != ' ' for symbol in sequence):
                return sequence[0]

    # Check diagonals (bottom-left to top-right): (similar logic as rows)
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            sequence = [board[row - i][col + i] for i in range(4)]
            if all(symbol == sequence[0] and symbol != ' ' for symbol in sequence):
                return sequence[0]
    
    return None

def check_for_draw():
    """Check if the board is full of symbols and there are no more empty places to make a move"""
    for row in board:
        if ' ' in row:
            return False
    return True


def toggle_player(current_player, player_1, player_2):
    """Toggle between the first and second player"""
    return player_2 if current_player == player_1 else player_1

# Confirming the start of the game
print("Welcome to Connect Four")
print("Press ENTER to start the game or ESC to exit")

while True:
    key_pressed = keyboard.read_event(suppress=True).name
    if key_pressed == 'enter':
        print("Starting the game...")
        
        print("Game started!\n")
        break
    elif key_pressed == 'esc':
        print("Exiting the game...")
        
        sys.exit()

# Prompt users to enter their names
name1 = input("Player 1 name: ")
while not name1:
    name1 = input("Please enter a valid name for Player 1: ")

name2 = input("Player 2 name: ")
while not name2:
    name2 = input("Please enter a valid name for Player 2: ")

# Create 2 instances of Player
player1 = Player(name1, 'X')
player2 = Player(name2, 'O')

# Starting game
connect_four(player1, player2)
