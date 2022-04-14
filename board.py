# Max Clingroth
# CSC 120 Tic Tac Toe
import sqlite3 as sq3
from os.path import exists


class Tic_Tac_Toe():
    # Creates a new board and runs the game
    def __init__(self):
        if exists('TIC_TAC_TOE.db'):
            self.db = sq3.connect('TIC_TAC_TOE.db')
        else:
            self.db = sq3.connect('TIC_TAC_TOE.db')
            cur = self.db.cursor()
            cur.execute('CREATE TABLE GAMES (game_id NUMBER PRIMARY KEY, '
                        'date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, result CHAR2 NOT NULL, '
                        'final_board CHAR2 NOT NULL);')
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        print('Welcome to Tic Tac Toe!')
        choice = self.main_menu()
        while choice != 0:
            if choice == 1:
                self.play()
            elif choice == 2:
                self.db_menu()
            choice = self.main_menu()
        print('Thanks for playing!')
        self.db.commit()
        self.db.close()

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

    # Runs one game
    def play(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        won = False
        player = 1
        cur = self.db.cursor()
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
                # Stores game in database
                high = 0
                if cur.execute('SELECT COUNT(*) from games;').fetchone()[0] > 0:
                    high = cur.execute('SELECT MAX(game_id) FROM games;').fetchone()[0] + 1
                final_board = ''
                for row in range(len(self.board)):
                    for col in range(len((self.board[row]))):
                        final_board += f'{self.board[row][col]}   '
                    final_board += 'n'
                cur.execute(f"INSERT INTO games (game_id, result, final_board)"
                            f" VALUES ({high}, 'Player {player} win', '{final_board}');")
            else:
                # Checks for a tie
                tie = True
                for row in range(len(self.board)):
                    for col in range(len(self.board[row])):
                        if self.check_mark(row, col):
                            tie = False
                if tie:
                    print('The game is a tie! Game Over!')
                    won = True
                    # Stores game in database
                    high = 0
                    if cur.execute('SELECT COUNT(*) from games;').fetchone()[0] > 0:
                        high = cur.execute('SELECT MAX(game_id) FROM games;').fetchone()[0] + 1
                    final_board = ''
                    for row in range(len(self.board)):
                        for col in range(len((self.board[row]))):
                            final_board += f'{self.board[row][col]}   '
                        final_board += '\n'
                    cur.execute(f"INSERT INTO games (game_id, result, final_board)"
                                f" VALUES ({high}, 'Tie', '{final_board}')")
            # Changes the player
            if player == 1:
                player = 2
            elif player == 2:
                player = 1

    # Displays the menu
    def main_menu(self):
        while True:
            try:
                choice = int(input('Select 1 to play, 2 to view previous games, or 0 to quit: '))
            except ValueError:
                print('*** Please enter an integer from 0 - 2 ***')
                continue
            if choice < 0 or choice > 2:
                print('*** Please enter an integer from 0 - 2 ***')
                continue
            else:
                return choice

    # Displays options for database
    def db_menu(self):
        choice = 1
        while choice != 0:
            try:
                choice = int(input('Select 1 to view all previous games,'
                                   ' 2 to view the board of a game,'
                                   ' 3 to delete a game, or 0 to return to main menu: '))
            except ValueError:
                print('*** Please enter an integer from 0 - 3 ***')
                continue
            if choice < 0 or choice > 3:
                print('*** Please enter an integer from 0 - 3 ***')
                continue
            self.db_options(choice)

    # Performs actions with the database
    def db_options(self, choice):
        cur = self.db.cursor()
        if choice == 1:
            print('GAME_ID, DATE, RESULT')
            if cur.execute('SELECT COUNT(*) from games;').fetchone()[0] == 0:
                print('No games in database')
            else:
                for row in cur.execute('SELECT game_id, date, result FROM games;'):
                    print(row)
        if choice == 2:
            again = 'y'
            while again.lower() != 'n':
                try:
                    id = int(input("Enter the id for the game you wish to view: "))
                except ValueError:
                    print('*** Please enter a valid integer ***')
                    continue
                try:
                    board = cur.execute(f'SELECT final_board FROM games '
                                        f'WHERE game_id = {id};').fetchone()[0]
                except TypeError:
                    print('*** Please select a valid game id ***')
                    continue
                board = board.replace('n', '\n')
                print(board)
                again = input('View another board? (y/n): ')
        if choice == 3:
            again = 'y'
            while again.lower() != 'n':
                try:
                    id = int(input("Enter the id for the game you wish to delete, cheater: "))
                except ValueError:
                    print('*** Please enter a valid integer ***')
                    continue
                try:
                    test = cur.execute(f'SELECT * FROM games WHERE game_id = {id}').fetchone()[0]
                except TypeError:
                    print('*** Please select a valid game id to delete ***')
                    continue
                cur.execute(f'DELETE FROM games WHERE game_id = {id}')
                print('Game Deleted')
                again = input('Delete another game, cheater? (y/n): ')


game = Tic_Tac_Toe()