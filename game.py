import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer  # Assuming there's a 'player.py' file with Player classes

class TicTacToe:
    def __init__(self):
        self.board = self.make_board()  # Initialize the board
        self.current_winner = None  # Track the current winner, if any

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]  # Create an empty board with 9 squares

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')  # Print the current state of the board

    @staticmethod
    def print_board_nums():
        # Print the numbers corresponding to each square
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter  # Place a player's letter in a square if it's empty
            if self.winner(square, letter):  # Check if the move resulted in a win
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check if a player has won after making a move
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]

        if all([s == letter for s in row]):  # Check the row
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]  # Check the column

        if all([s == letter for s in column]):
            return True

        if square % 2 == 0:  # If the move is in a diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board  # Check if there are any empty squares on the board

    def num_empty_squares(self):
        return self.board.count(' ')  # Count the number of empty squares

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]  # Return a list of available moves


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)  # Get O player's move
        else:
            square = x_player.get_move(game)  # Get X player's move

        if game.make_move(square, letter):  # Make the move

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:  # Check if there's a winner
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')

# Main execution block
if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')  # Create an instance of SmartComputerPlayer with letter 'X'
    o_player = HumanPlayer('O')  # Create an instance of HumanPlayer with letter 'O'
    t = TicTacToe()  # Create an instance of TicTacToe
    play(t, x_player, o_player, print_game=True)  # Start the game with specified players