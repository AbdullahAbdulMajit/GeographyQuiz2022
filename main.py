#This code is used to import funtions and modules that are pre-built from the tkinter library.
from tkinter import * 

#VARIABLES - Objects assigned to a variable can be referred by the variable.
names = []

#This is my Home window component, users will be directed to this window at launch.
class HomeWindow:

  def __init__(self, parent):

    #This is used to create a frame where widgets can be used to sit on.
    self.frame = Frame(parent, pady = 75)
    self.frame.grid()

    #This is where I'll be setting up my heading for my program.
    self.title = Label(self.frame, text = "Welcome to my Geography Quiz!⁽²⁰²²⁾", font = ("30"))
    self.title.grid(row = 0, padx = 80, pady = 30)

    #Adding an extra label to give tips on how to proceed with the porgram.
    self.info = Label(self.frame, text = "TIP: To play the game enter your name below and click START.\nFor instructions on how to play the game, click '?'.")
    self.info.grid(row = 1, pady = 20)

    #This is what users will use to put undersnames.
    self.name = Entry(self.frame)
    self.name.grid(row = 2, pady = 20)

    #Button that says START allowing people to move to the next window when clicked.
    self.button = Button(self.frame, text = "START")
    self.button.grid(row = 3)
    

#### MAIN ####
#This makes this file the starter file.
if __name__ == "__main__": 

    #This code makes the window pop up when launched.
    root = Tk() 

    #The code below is used to name the title bar.
    root.title("Basic Geography Quiz 2022") 

    #HomeWIndow class becomes the root window when launched.
    home_object = HomeWindow(root) 

    #Size of the windows at launch.
    root.geometry("500x500")

    root.resizable(False, False)

    #To keeps the window on it must be on loop.
    root.mainloop() 


    