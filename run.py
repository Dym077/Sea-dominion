import random
"""
The class for the game board setting all parameterns for player and computer.
"""


class GameBoard:
    def __init__(self):
        # Initialize the game board with default settings
        self.board_size = 5
        self.ship_size = 3
        self.player_board = [
            [" " for _ in range(self.board_size)]
            for _ in range(self.board_size)
        ]
        self.computer_board = [
            [" " for _ in range(self.board_size)]

            for _ in range(self.board_size)
        ]
        self.player_turns = 20
        self.computer_turns = 20
        self.player_ships = 3  # Track remaining ships for player
        self.computer_ships = 3
        self.player_score = 0  # Track the score for the player
        self.computer_score = 0  # Track the score for the computer

    def get_username(self):
        input_valid = False
        username = ""
        while input_valid is False:
            user_input = input("Enter Your username: ")
            if len(user_input) < 4:
                print("Please enter a minimum of 4 characters")
            else:
                input_valid = True
                username = user_input
        return username

    def display_board(self, board, is_player=True):
        # Displays the game board with player and computer boards.
        print("   0 1 2 3 4")
        for i, row in enumerate(board):
            if not is_player:
                # Is it the computer's board, the ships will be hidden
                row = [" " if cell == "€" else cell for cell in row]
            print(f"{i} |{'|'.join(row)}|")

    def place_ships(self, board, ships):
        # Places ships on board randomly, ensuring no overlaps.
        for _ in range(ships):
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            while board[row][col] == "€":
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)
            board[row][col] = "€"

    def validate_input(self, row, col):
        # Validates the input coordinates
        return 0 <= row < self.board_size and 0 <= col < self.board_size

    def make_shot(self, board, row, col, player):
        # Execute player's and computer's shot on board and update status
        if board[row][col] == "€":
            print(f"\n{player} HITS!")
            board[row][col] = "X"
            return True
        else:
            print(f"\n{player}MISS!")
            board[row][col] = "O"
            return False

    def display_instructions(self):
        # Show welcome message, game instructions and information to player
        print("\nSea Dominion - A battleships game.\n")
        print("Game rules:")
        print("1. This game has two boards, one for each player.")
        print("2. The boards are marked with the numbers 0 - 4.")
        print("3. The 3 ships are hidden - You have 20 attempts to sink them.")
        print("4. Guess a row and a column between 0 and 4.")
        print("5. When You HIT a ship, You will see 'X'.")
        print("6. If You MISS a ship, You will see 'O'.")
        print("7. Your ships are displayed as '€'.")
        print("8. You can type 'exit' to quit the game anytime.")
        print("\nBegin sea-battle!\n")

    def play_game(self):
        # Primary game loop with turns and outcomes
        while True:
            self.display_instructions()
            player_name = self.get_username()

            self.place_ships(self.player_board, self.player_ships)
            self.place_ships(self.computer_board, self.computer_ships)

            player_guess = set()
            computer_guess = set()

            while (
                self.player_turns > 0
                and self.computer_turns > 0
                and self.player_ships > 0
                and self.computer_ships > 0
            ):
                # Player's turn
                print(f"\n{player_name}'s board:")
                self.display_board(self.player_board)

                while True:
                    error_m = "This coordinate is already tried. Please try again!"
                    message = "Enter row (0-4) or quit game by typing 'exit':"
                    row_input = input(message)
                    if row_input.lower() == "exit":
                        break

                    col_input = input("Enter column (0-4): ")
                    try:
                        row = int(row_input)
                        col = int(col_input)
                        if not self.validate_input(row, col):
                            print("Coordinates are invalid! Please try again!")
                            continue
                        if (row, col) in player_guess:
                            print(error_m)
                            continue
                        player_guess.add((row, col))
                        player_hit = self.make_shot(self.computer_board, row, col)
                        if player_hit:
                            self.computer_ships -= 1
                            self.player_score += 1  # Player's score is updated
                        break
                    except ValueError:
                        print("Interesting, but You should enter a number!")
                if row_input.lower() == "exit":
                    break
                while True:
                    computer_row = random.randint(0, self.board_size - 1)
                    computer_col = random.randint(0, self.board_size - 1)
                    if (computer_row, computer_col) in computer_guess:
                        continue
                    computer_guess.add(
                        (computer_row, computer_col))
                    computer_hit = self.make_shot
                    (self.player_board, computer_row, computer_col, 'Computer')
                    if computer_hit:
                        self.player_ships -= 1
                        self.computer_score += 1
                        # Computer's score gets updated
                    break

                self.player_turns -= 1
                self.computer_turns -= 1
                print(f"""\nTurns left:
{player_name} = {self.player_turns}, Computer = {self.computer_turns}
Scores:
{player_name} = {self.player_score}, Computer = {self.computer_score}""")

            print("\nGame Over!")
            print(f"{player_name}'s Board:")
            self.display_board(self.player_board)
            print("\nComputer's Board:")
            self.display_board(self.computer_board, is_player=False)

            if self.player_ships == 0:
                print("""\nYou lost! All Your ships have been sunk!""")
            elif self.computer_ships == 0:
                print(f"""\nGreat {player_name}!
                All the computer's ships have been sunk!""")
            else:
                print("\nBoth players have ships remaining.")
            # Display score for player and computer
            print(f"""\nScores:
{player_name} = {self.player_score}, Computer: {self.computer_score}""")

            while True:
                play_again = input("\nPlay another game? (yes/no): ")
                if play_again.lower() in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")

            if play_again.lower() != "yes":
                print(f"Thanks for playing {player_name}! We'll be sea-ing You again.")
                break
            else:
                # Restart the game with a new round
                self.restart_game()

    def restart_game(self):
        # Restart the game paramenters for new round
        self.player_board = [
            [" " for _ in range(self.board_size)]
            for _ in range(self.board_size)
        ]
        self.computer_board = [
            [" " for _ in range(self.board_size)]
            for _ in range(self.board_size)
        ]
        self.player_turns = 20
        self.computer_turns = 20
        self.player_ships = 3
        self.computer_ships = 3
        self.player_score = 0  # Player's score is reset
        self.computer_score = 0  # Computer's score is reset


if __name__ == "__main__":
    game = GameBoard()
    game.play_game()
