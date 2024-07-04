import tkinter as tk
from tkinter import messagebox
from game_logic import Player, GameLogic

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.create_menu()
        self.game_logic = GameLogic()
        self.create_players()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.reset_game)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.root.quit)

    def create_players(self):
        player1 = Player("Player 1", "X")
        player2 = Player("Player 2", "O")
        self.game_logic.add_player(player1)
        self.game_logic.add_player(player2)

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('normal', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.game_logic.make_move(row, col):
            self.update_board()
            winner = self.game_logic.check_winner()
            if winner:
                self.highlight_winner(winner)
                messagebox.showinfo("Game Over", f"{winner.name} wins!")
                self.reset_game()
            elif self.game_logic.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.game_logic.switch_player()

    def update_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=self.game_logic.board[row][col])

    def highlight_winner(self, winner):
        for combination in self.game_logic.winning_combinations:
            if all(self.game_logic.board[row][col] == winner.symbol for row, col in combination):
                for row, col in combination:
                    self.buttons[row][col].config(bg="lightgreen")

    def reset_game(self):
        self.game_logic.reset_board()
        self.update_board()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(bg="SystemButtonFace")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
