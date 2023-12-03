from tkinter import *
from v4game_grid import GridDuel
from snake2 import start_game

class StartGame():
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
        self.w1.title('Choose a Game to Play 🎮')
        self.w1.maxsize(910,539)
        #A Canvas widget, for our window background
        self.background = PhotoImage(file='wallpaper1.png')
        self.bcanvas = Canvas(self.w1, width=910, height=539)  
        self.bcanvas.pack( expand=True, fill='both', anchor='center')
        self.bcanvas.create_image(0,0, image=self.background,anchor='nw')
        #Two buttons for single player and multiplayer.
        self.singleplay_button = Button(self.w1, text = "Grid Duel", fg = "#55557f", font =( "Comic Sans MS", 16), activebackground='#aaddfe', bg='#aaddfe')
        self.singleplay_button.place(x = 270, y = 180, width = 360, height = 52)
        self.singleplay_button['command'] = self.game_gridDuel
        self.Twoplay_button = Button(self.w1, text = "Python's Playground", fg = "#55557f", font =( "Comic Sans MS", 16), activebackground='#aaddfe', bg='#aaddfe')
        self.Twoplay_button.place(x = 270, y = 300, width = 360, height = 52)
        self.Twoplay_button['command'] = self.game_pythonsPlayground

    def game_gridDuel(self):
        self.remove()
        self.game = GridDuel()

    def game_pythonsPlayground(self):
        self.remove()
        start_game(1)

if __name__ == '__main__':
    app = StartGame()