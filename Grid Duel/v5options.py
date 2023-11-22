
from tkinter import *
from tkinter import messagebox  #import message box libray


class Options():
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
        self.w1.title('Options')
        self.w1.maxsize(910,539)
        #A Canvas widget, for our window background
        self.background = PhotoImage(file='wallpaper1.png')
        self.bcanvas = Canvas(self.w1, width=910, height=539)  
        self.bcanvas.pack( expand=True, fill='both', anchor='center')
        self.bcanvas.create_image(0,0, image=self.background,anchor='nw')
        #Buttons
        self.changepass_button = Button(self.w1, text = "Change Password", fg = "#55557f", font = ("Comic Sans MS", 16), activebackground='#aaddfe', bg='#aaddfe')
        self.changepass_button.place(x = 320, y = 130, width = 240, height = 42)
        self.changepass_button['command'] = self.change_password
        self.help_button = Button(self.w1, text = "User Guide", fg = "#55557f", font = ("Comic Sans MS", 16), activebackground='#aaddfe', bg='#aaddfe')
        self.help_button.place(x = 320, y = 290, width = 240, height = 42)
        self.help_button['command'] = self.open_userguide
        self.back_button = Button(self.w1, text = "BACK", fg = "#55557f", font = ("Comic Sans MS", 16), activebackground='#aaddfe', bg='#aaddfe')
        self.back_button.place(x = 360, y = 380, width = 150, height = 42)
        self.back_button['command'] = self.back_Options
        self.scores_button = Button(self.w1, text = "View scores", fg = "#55557f", font = ("Comic Sans MS", 16), activebackground='#aaddfe', bg='#aaddfe')
        self.scores_button.place(x = 320, y = 210, width = 240, height = 42)
        self.scores_button['command'] = self.open_scores

    def change_password(self):
        #opens log in window
        self.remove()
        from v1log_in import LogIn
        self.login_window = LogIn()

    def open_scores(self):
        #shows a message box for wins, loses, draws
        messagebox.showinfo(title="Scores ", message="Wins = {} Draws = {}")

    def open_userguide(self):
        #opens a message box for Options help
        messagebox.showinfo(title="User Guide", message="""✨Welcome to Grid duel |now with Snake!|  ✨\nIts super easy, just align Xs or Os in a straight line 😊!\nAre you ready to become the ultimate champion? 😎 """)

    def back_Options(self):
        #opens the game_home window and closes Options
        self.remove()
        from v2game_home import GameHome    #prevent circular import traceback
        self.signin_window = GameHome()
