from tkinter import *
from tkinter import messagebox  #import message box libray
from v2game_home import GameHome
from ourUserDatabase import *
class LogIn():
    def __init__(self):
        self.gui()
        self.run()

    def gui(self ):
        #This function defines our window, and all the widgets it'll contain
        #Window Widget
        self.w1 = Tk()  #the tkinter window widget, w1, will be an instance attribute, hence the "self."
        self.w1.geometry('910x539')
        self.w1.title('Log In Page')
        self.w1.maxsize(910,539)    #We set a  max size to prevent scaling of the window above our background image size.
        #A Canvas widget, for our window background
        self.background = PhotoImage(file='wallpaper1.png')
        self.bcanvas = Canvas(self.w1, width=910, height=539)  
        self.bcanvas.pack( expand=True, fill='both', anchor='center')
        self.bcanvas.create_image(0,0, image=self.background,anchor='nw')   #set image in canvas
        #Entry boxes
        self.username_entry = Entry(self.w1, fg = "#55557f", bg ='#aaddfe', font = ( "Comic Sans MS", 16))
        self.username_entry.place(x = 390, y = 200, width = 340, height = 42)
        self.username_entry.insert(0, "Enter your user name here")  #Place holder text
        self.password_entry = Entry(self.w1, fg = "#55557f", bg ='#aaddfe', font = ( "Comic Sans MS", 16), show='*')
        self.password_entry.place(x = 390, y = 300, width = 340, height = 42)
        ## self.password_entry.insert(0, "Enter your Password here")    #Place holder text
        #Buttons
        self.newUser_button = Button(self.w1, text = "new user", fg = "#55557f", font = ( "Comic Sans MS", 14), activebackground='#aaddfe', bg='#aaddfe' )
        self.newUser_button.place(x = 230, y = 370, width = 150, height = 52)
        self.newUser_button['command'] = self.create_newuser
        self.signIn_button = Button(self.w1, text = "Sign in", fg = "#55557f", font = ( "Comic Sans MS", 14),activebackground='#aaddfe', bg='#aaddfe')
        self.signIn_button.place(x = 650, y = 370, width = 150, height = 52)
        self.signIn_button['command'] = self.signIn
        #labels
        self.label_username = Label(self.w1, text = "User name", anchor='w', fg = "#55557f",bg='#0f181d' ,font = ( "Comic Sans MS", 16))
        self.label_username.place(x = 230, y = 210, width = 120, height = 22)
        self.label_password = Label(self.w1, text = "Password", anchor='w', fg = "#55557f",bg='#0f181d', font = ( "Comic Sans MS", 16))
        self.label_password.place(x = 230, y = 310, width = 100, height = 32)
        self.label_noAccount = Label(self.w1, text = "No account?", anchor='w', fg = "#55557f",bg='#0f181d', font = ( "Comic Sans MS", 16))
        self.label_noAccount.place(x = 90, y = 380, width = 140, height = 32)
        self.label_ihaveAccount = Label(self.w1, text = "I have an account", anchor='w', fg = "#55557f",bg='#0f181d', font = ( "Comic Sans MS", 16))
        self.label_ihaveAccount.place(x = 450, y = 380, width = 200, height = 32)
        self.label_welcome = Label(self.w1, text = "Welcome to Grid Duel", anchor='w', fg = "#55557f",bg='#0f181d', font = ( "Comic Sans MS", 18))
        self.label_welcome.place(x = 320, y = 100, width = 270, height = 22)
    #run the window
    def run (self):
        self.w1.mainloop()
    #destroy the window
    def remove (self):
        self.w1.destroy()

    #create a new user by adding the name and password to the db
    def create_newuser(self):
       
        newUserName = self.username_entry.get()
        newUserPassword = self.password_entry.get()
        #check if the credentials already exist, and proceed normally if they do
        if self.check(newUserName, newUserPassword):
            self.remove()
            #open the next window (game_home)
            self.signin_window = GameHome()
        else:
            add_data(newUserName,newUserPassword)
            self.remove()
            self.signin_window = GameHome()
            
        

    def signIn(self):
        #verify that the details entered are in the db
        userName = self.username_entry.get()
        userPassword = self.password_entry.get()
        if self.check(userName, userPassword):
            self.remove()
            #opens the next window (game_home)
            self.signin_window = GameHome()
        else:
            messagebox.showerror(title='Access Denied', message='Credentials not found!')
            
    def check(self, a,b):
        return query_database(a,b)

if __name__ == '__main__':
    app = LogIn()