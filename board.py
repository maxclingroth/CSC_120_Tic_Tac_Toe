# Max Clingroth
# CSC 120 Tic Tac Toe


class Tic_Tac_Toe():
    # Creates a new board and runs the game
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        won = False
        player = 1
        # Loops each turn
        while not won:
            self.display()
            print()
            print(f'Player {player}, make your move')
            # Input Validation
            try:
                row = int(input('Enter row nos (0-2): '))
                col = int(input('Enter col nos (0-2): '))
            except ValueError:
                print('*** Invalid Entry: Please enter an integer 0-2 ***')
                continue
            # Input Validation
            if row < 0 or row > 2 or col < 0 or col > 2:
                print('*** Invalid Entry: Please enter an integer 0-2 ***')
                continue
            if self.check_mark(row, col):
                print()
                print(f'Player {player} added mark at location {row}, {col}')
                self.place_mark(row, col, player)
            # Input Validation
            else:
                print(f'*** Board[{row}][{col}] has already been selected. Please '
                      f'select somewhere else ***')
                continue
            # Checks if player has won
            if self.check_win(player):
                print(f'Player {player} wins! Game Over!')
                won = True
            # Checks for a tie
            tie = True
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.check_mark(row, col):
                        tie = False
            if tie:
                print('The game is a tie! Game Over!')
                won = True
            # Changes the player
            if player == 1:
                player = 2
            elif player == 2:
                player = 1

    # Displays the board
    def display(self):
        print('Printing board...')
        for row in self.board:
            print(row)

    # Checks if the selected square is taken
    def check_mark(self, row, col):
        if self.board[row][col] == '-':
            return True
        else:
            return False

    # Places a mark at selected square
    def place_mark(self, row, col, player):
        if player == 1:
            self.board[row][col] = 'X'
        elif player == 2:
            self.board[row][col] = 'O'

    # Checks if a player has won the game
    def check_win(self, player):
        if player == 1:
            for row in self.board:
                if row[0] == 'X' and row[1] == 'X' and row[2] == 'X':
                    return True
            for col in range(len(self.board[0])):
                if (self.board[0][col] == 'X' and self.board[1][col] == 'X'
                        and self.board[2][col] == 'X'):
                    return True
            if (self.board[0][0] == 'X' and self.board[1][1] == 'X'
                    and self.board[2][2] == 'X'):
                return True
            if (self.board[0][2] == 'X' and self.board[1][1] == 'X'
                    and self.board[2][0] == 'X'):
                return True
            return False
        if player == 2:
            for row in self.board:
                if row[0] == 'O' and row[1] == 'O' and row[2] == 'O':
                    return True
            for col in range(len(self.board[0])):
                if (self.board[0][col] == 'O' and self.board[1][col] == 'O'
                        and self.board[2][col] == 'O'):
                    return True
            if (self.board[0][0] == 'O' and self.board[1][1] == 'O'
                    and self.board[2][2] == 'O'):
                return True
            if (self.board[0][2] == 'O' and self.board[1][1] == 'O'
                    and self.board[2][0] == 'O'):
                return True
            return False


game = Tic_Tac_Toe()