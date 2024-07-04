class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class GameLogic:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = None
        self.players = []
        self.winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (0, 2)],
        ]

    def add_player(self, player):
        self.players.append(player)
        if len(self.players) == 1:
            self.current_player = player

    def switch_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def is_valid_move(self, row, col):
        return self.board[row][col] == ''

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player.symbol
            return True
        return False

    def check_winner(self):
        for combination in self.winning_combinations:
            symbols = [self.board[row][col] for row, col in combination]
            if symbols[0] != '' and symbols.count(symbols[0]) == 3:
                return self.current_player
        return None

    def check_tie(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def reset_board(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
