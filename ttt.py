'''
| X | O | O |
|---+---+---|
| O | X | X |
|---+---+---|
| X | O | X |
'''


def main():
    game = Game()
    game.start_game()

class Game(object):
    def __init__(self):
        self._player_one = Player('p1', 'X')
        self._player_two = Player('p2', 'O')
        self._board = Board()

        self._counter = 0

    def start_game(self):
        self._board.print_board()

        has_won = False
        currplayer = self._player_one

        while not has_won and self._counter < 9:
            if self._counter % 2 == 0:
                currplayer = self._player_one
            else:
                currplayer = self._player_two

            self._counter += 1
            has_won = self.move(currplayer)

        if has_won:
            print(currplayer.player_number + ' won!')
        else:
            print('This is a draw.')

    def move(self, currplayer):
        is_valid_cell = False
        while not is_valid_cell:
            player_input = input("It\'s " + currplayer.player_number + "\'s turn. Please type desired number: ")
            try:
                player_move = int(player_input)
                if (player_move < 9 and player_move >= 0) and self._board.is_cell_empty(player_move):
                    break
                elif player_move in range(0,9):
                    print('Please choose different position! The position is already taken.')
                else:
                    print('Please type available number inside the board.')
            except ValueError:
                print('Please enter a valid integer.')


        self._board.update_cell(player_move, currplayer.player_symbol)
        self._board.print_board()

        return self._board.has_winner()

class Player(object):
    def __init__(self, player_number, player_symbol):
        self.player_number = player_number
        self.player_symbol = player_symbol

class Board(object):
    def __init__(self):
        self._board = self._init_board()

    def _init_board(self):
        return [[i, str(i)] for i in range(0, 9)]

    def update_cell(self, num, player_symbol):
        self._board[num][1] = player_symbol

    def is_cell_empty(self, num):
        # We assume that the players' symbols are not integers.
        try:
            int(self._board[num][1])
            return True
        except ValueError:
            return False

    def has_winner(self):
        row  = self._board[0][1]==self._board[1][1]==self._board[2][1] or \
               self._board[3][1]==self._board[4][1]==self._board[5][1] or \
               self._board[6][1]==self._board[7][1]==self._board[8][1]
        col  = self._board[0][1]==self._board[3][1]==self._board[6][1] or \
               self._board[1][1]==self._board[4][1]==self._board[7][1] or \
               self._board[2][1]==self._board[5][1]==self._board[8][1]
        diag = self._board[0][1]==self._board[4][1]==self._board[8][1] or \
               self._board[2][1]==self._board[4][1]==self._board[6][1]

        return row or col or diag

    def print_board(self):
        print(' | '.join([self._board[i][1] for i in range(0, 3)]))
        print('--+---+--')
        print(' | '.join([self._board[i][1] for i in range(3, 6)]))
        print('--+---+--')
        print(' | '.join([self._board[i][1] for i in range(6, 9)]))

if __name__ == "__main__":
    main()
