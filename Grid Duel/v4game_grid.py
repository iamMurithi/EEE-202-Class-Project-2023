from tkinter import *
from tkinter import messagebox
class GridDuel:
        def __init__(self):
            self.w1 = Tk()
            self.w1.title("GridDuel")

            self.current_player = 'X'
            self.board = [' ' for _ in range(9)]

            self.buttons = [None] * 9

            for i in range(9):
                row, col = divmod(i, 3)
                self.buttons[i] = Button(self.w1, text='', width=12, height=5,font=("Comic Sans MS", 16), bg='#aaddfe', activebackground='#aaddfe',
                                            command=lambda i=i: self.make_move(i))
                self.buttons[i].grid(row=row, column=col)
            self.run()

        def make_move(self, i):
            if self.board[i] == ' ':
                self.board[i] = self.current_player
                self.buttons[i].config(text=self.current_player)
                if self.check_win(self.current_player):
                    messagebox.showinfo(
                        "Grid Duel", f"Player {self.current_player} wins!")
                    self.reset_game()
                elif ' ' not in self.board:
                    messagebox.showinfo("Grid Duel", "It's a draw!")
                    self.reset_game()
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'

        def check_win(self, player):
            winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]
            for combo in winning_combinations:
                if all(self.board[i] == player for i in combo):
                    return True
            return False

        def reset_game(self):
            for i in range(9):
                self.board[i] = ' '
                self.buttons[i].config(text='')
            self.current_player = 'X'

        def run(self):
            self.w1.mainloop()

if __name__ == "__main__":
    game = GridDuel()