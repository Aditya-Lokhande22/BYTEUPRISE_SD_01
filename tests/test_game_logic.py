import unittest
from game_logic import Player, GameLogic

class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.game = GameLogic()
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.game.add_player(self.player1)
        self.game.add_player(self.player2)

    def test_initial_board(self):
        expected_board = [['' for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.game.board, expected_board)

    def test_add_player(self):
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual(self.game.players[0].name, "Player 1")
        self.assertEqual(self.game.players[1].name, "Player 2")

    def test_valid_move(self):
        self.assertTrue(self.game.is_valid_move(0, 0))
        self.game.make_move(0, 0)
        self.assertFalse(self.game.is_valid_move(0, 0))

    def test_make_move(self):
        self.assertTrue(self.game.make_move(0, 0))
        self.assertEqual(self.game.board[0][0], self.player1.symbol)

    def test_switch_player(self):
        self.assertEqual(self.game.current_player, self.player1)
        self.game.switch_player()
        self.assertEqual(self.game.current_player, self.player2)

    def test_check_winner(self):
        self.game.board = [
            ['X', 'X', 'X'],
            ['', '', ''],
            ['', '', '']
        ]
        self.assertEqual(self.game.check_winner(), self.player1)

    def test_check_tie(self):
        self.game.board = [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertTrue(self.game.check_tie())

    def test_reset_board(self):
        self.game.board = [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.game.reset_board()
        expected_board = [['' for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.game.board, expected_board)


if __name__ == '__main__':
    unittest.main()
