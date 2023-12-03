from tkinter import *
from tkinter import messagebox
from v2game_home import *
from ourScoreDatabase import *
# Import SQLite for database functionality
import sqlite3

# Initialize the database connection once
scoreDB = sqlite3.connect('ScoreDatabase.db')
score_cursor = scoreDB.cursor()

# Define our class
class GridDuel:
    def __init__(self):
        # Initialize the main window
        self.w1 = Tk()
        self.w1.title("GridDuel")
        
        # Initialize the game variables
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]

        # Create buttons for the game grid
        self.buttons = [None] * 9
        for i in range(9):
            row, col = divmod(i, 3)
            self.buttons[i] = Button(self.w1, text='', width=12, height=5,
                                     font=("Comic Sans MS", 16), 
                                     bg='#aaddfe', activebackground='#aaddfe',
                                     command=lambda i=i: self.make_move(i))
            self.buttons[i].grid(row=row, column=col)
        
        # Display user guide
        self.userguide()
        
        # Run the main loop
        self.run()

    def make_move(self, i):
        # Handle player moves
        if self.board[i] == ' ':
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            
            # Check for a win
            if self.check_win(self.current_player):
                messagebox.showinfo("Grid Duel", f"Player {self.current_player} wins!")
                
                # Update the scores database
                update_scores('wins')
                
                # Reset the game
                if messagebox.askyesno(title='Game Over', message='Play again?'):
                    self.reset_game()
                else:
                    self.remove()
                    self.back()
                    
            # Check for a draw
            elif ' ' not in self.board:
                messagebox.showinfo("Grid Duel", "It's a draw!")
                update_scores('draws')
                
                # Reset the game
                if messagebox.askyesno(title='Game Over', message='Play again?'):
                    self.reset_game()
                else:
                    self.remove()
                    self.back()
            else:
                # Switch players
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def userguide(self):
        # Display a user guide message box
        messagebox.showinfo(title="User Guide", message="""✨just align Xs or Os in a straight line 😊!""")

    def check_win(self, player):
        # Check if a player has won
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def reset_game(self):
        # Reset the game board and player
        for i in range(9):
            self.board[i] = ' '
            self.buttons[i].config(text='')
        self.current_player = 'X'

    def remove(self):
        # Close the game window
        self.w1.destroy()
        
    def back(self):
        # Go back to the main menu
        self.back_to_main = GameHome()

    def run(self):
        # Run the main loop
        self.w1.mainloop()

# Run the game if executed as a standalone script
if __name__ == "__main__":
    game = GridDuel()
