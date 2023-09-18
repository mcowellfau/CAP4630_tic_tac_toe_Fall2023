import math
import time
from player import MyHumanPlayer, MyRandomComputerPlayer, MySmartComputerPlayer

class MyTicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]

        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]

        if all([s == letter for s in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

def play_game(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'O'  # Start with player 'O'
    while game.empty_squares():
        if letter == 'X':
            square = x_player.make_move(game)
        else:
            square = o_player.make_move(game)

        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'X' if letter == 'O' else 'O'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')

def play_another_round():
    # Function to ask if the user wants to play another round
    while True:
        choice = input("Do you want to play another round? (y/n): ")
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print("Invalid choice. Please enter 'y' for yes or 'n' for no.")

# Main execution block
if __name__ == '__main__':
    play_again = True
    while play_again:
        player_X = MyHumanPlayer('X')  # User plays as 'X'
        player_O = MySmartComputerPlayer('O')  # Computer plays as 'O'
        my_game = MyTicTacToe()  # Create an instance of MyTicTacToe
        print("Welcome to Tic-Tac-Toe! Choose a square based on the printed board to begin. Get 3 in a row to win!")
        play_game(my_game, player_X, player_O, print_game=True)  # Start the game with specified players

        play_again = play_another_round()

        if play_again:
            my_game = MyTicTacToe()  # Reset the game if the user chooses to play again