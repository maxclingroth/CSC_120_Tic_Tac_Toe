# Max Clingroth
# CSC 120 Tic Tac Toe


class Tic_Tac_Toe():
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def display(self):
        print('Printing board...')
        for row in self.board:
            print(row)

    def check_mark(self, row, col):
        if self.board[row][col] == '-':
            return True
        else:
            return False

    def place_mark(self, row, col, player):
        if player == 1:
            self.board[row][col] = 'X'
        elif player == 2:
            self.board[row][col] = 'O'

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