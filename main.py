#This code is used to import funtions and modules that are pre-built from the tkinter library.
from tkinter import * 

#VARIABLES - Objects assigned to a variable can be referred by the variable.
names = []

global questions
questions =  {
  "q1" : ["Is the Vatican City is the smallest country?", 'Yes', 'No', 1],
  "q2" : ["Is Mount Fuji the tallest mountain in the world", 'Yes', 'No', 2]
}

#This is my Home window component, users will be directed to this window at launch.
class HomeWindow:

  def __init__(self, parent):

    #This is used to create a frame where widgets can be used to sit on.
    self.frame = Frame(parent, pady = 75)
    self.frame.grid()

    #This is where I'll be setting up my heading for my program.
    self.title = Label(self.frame, text = "Welcome to my Geography Quiz!⁽²⁰²²⁾", font = ("30"))
    self.title.grid(row = 0, padx = 100, pady = 30)

    #Adding an extra label to give tips on how to proceed with the porgram.
    self.info = Label(self.frame, text = "TIP: To play the game enter your name below and click START.\nFor instructions on how to play the game, click '?'.")
    self.info.grid(row = 1, pady = 20)

    #This is what users will use to put undersnames.
    self.name = Entry(self.frame)
    self.name.grid(row = 2, pady = 20)

    #Button that says START allowing people to move to the next window when clicked.
    self.button = Button(self.frame, text = "START", command = self.question_window)
    self.button.grid(row = 3)

    #Button that shows '?' that redirects to a pop up page that helps with the quiz.
    self.help = Button(self.frame, text = " ? ", command = self.to_help)
    self.help.grid(row = 4, pady  = 50)

    
  #Function that makes the pop up window and is linked to the above code.
  def to_help(self):
    
    toplevel = Toplevel(root)
    
    toplevel.geometry("500x300")

    toplevel.resizable(False, False)

    toplevel.title("HELP PAGE")
    
    self.helptitle = Label(toplevel, text = "NEED HELP?", font = ("30"))
    self.helptitle.grid(row = 0, padx = 185, pady = 50)

    self.helpinfo = Label(toplevel, text = "- Read the  question carefully.\n\n- Choose from the 'Yes' option if you agree or 'No' option if you disagree\n\n- Have fun!")
    self.helpinfo.grid(row = 1)

    
  #Function that stores names inputted from users.
  def stored_names(self):
    username = self.name.get()
    names.append(username) #stores input to the name list variable
    print(names)
    

  def question_window(self):
    self.frame.destroy()
    self.question_window = Questions(root)
    

class Questions:

  def __init__(self, parent):

    self.var1 = IntVar()

    self.frame = Frame(parent)
    self.frame.grid()

    self.question = Label(self.frame, text = questions.get("q1")[0])
    self.question.grid(row = 1)

    self.button1 = Radiobutton(self.frame, text = questions.get("q1")[1], value = 1, indicator = 0, variable = self.var1)
    self.button1.grid(row = 2, column = 1)

    self.button2 = Radiobutton(self.frame, text = questions.get("q1")[2], value = 2, indicator = 0, variable = self.var1)
    self.button2.grid(row = 2, column = 2)


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


    