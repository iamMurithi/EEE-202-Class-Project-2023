from tkinter import *
from v3start_game import StartGame
from v5options import Options
class GameHome():
    def __init__(self):
        self.gui()
        self.run()
    def run (self):
        self.w1.mainloop()
    def remove (self):
        self.w1.destroy()
    def gui(self):
        #This function defines our window, and all the widgets it'll contain
        #Window Widget
        self.w1 = Tk()
        self.w1.geometry('910x539')
        self.w1.title("Welcome to Grid Duel & Python's Playground")
        self.w1.maxsize(910,539)
        #A Canvas widget, for our window background
        self.background = PhotoImage(file='wallpaper1.png')
        self.bcanvas = Canvas(self.w1, width=910, height=539)  
        self.bcanvas.pack( expand=True, fill='both', anchor='center')
        self.bcanvas.create_image(0,0, image=self.background,anchor='nw')
        #Our 3 buttons for start game, options, and quit
        self.startGame_button = Button(self.w1, text = "Start a new game", fg = "#55557f", font = ("Comic Sans MS", 16), activebackground='#aaddfe', bg='#aaddfe')
        self.startGame_button.place(x = 300, y = 130, width = 290, height = 62)
        self.startGame_button['command'] = self.start_game
        self.options_button = Button(self.w1, text = "Options", fg = "#55557f", font = ("Comic Sans MS", 16), activebackground='#aaddfe', bg='#aaddfe')
        self.options_button.place(x = 300, y = 250, width = 290, height = 62)
        self.options_button['command'] = self.open_options
        self.quit_button = Button(self.w1, text = "Quit", fg = "#55557f", font = ("Comic Sans MS", 16), activebackground='#aaddfe', bg='#aaddfe')
        self.quit_button.place(x = 300, y = 380, width = 290, height = 62)
        self.quit_button['command'] = self.quit_game

    def start_game(self):
        #opens the next window (start_game)
        self.remove()
        self.gamehome_window = StartGame()

    def open_options(self):
        #opens the options window
        self.remove()
        self.options_window = Options()

    def quit_game(self):
        self.remove()

if __name__ == '__main__':
    app = GameHome()