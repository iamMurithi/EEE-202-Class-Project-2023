"""
Grid Duel (ft. Python's Playground) . Simple Computer Game with GUI.

Mogoa Duncan Begi: J174/1057/2022
Mwenda Victor Murithi: J174/1037/2022


Our project consists of the following modules:
    maingui.py          --> This script. initialises the first window instance
    v1log_in.py         --> Contains the Class 'LogIn', that defines the Log in page
    v2game_home.py      --> Contains the Class 'GameHome' that defines the Home page
    v3start_game.py     --> Contains the Class 'StartGame' that defines the Choose-a-game page
    v4game_grid.py      --> Contains the Class 'GridDuel' that defines game 1 : Grid Duel
    snake2.py           --> Contains functions that define game 2 : Python's Playground
    v5options.py        --> Contains the Class 'Options' that defines the Options Page
    
Our Project contains the following assets:
    wallpaper1.png      --> The image file used as the window background in Log in, Home, Choose-a-game and Options pages
    UserDatabase.db     --> The database containing our user credentials, i.e the names and passwords
    scoreDatabase.db    --> The database that stores the wins and draws everytime game 1 (Grid duel) is ran

"""
from v1log_in import LogIn
class App:
    def __init__(self):
        # Initialize the main window
        self.login_window = LogIn()   
if __name__ == '__main__':
    app = App()
