import tkinter as tk

# create BaseClass to use as general template for the other classes created:
# the classes Credits, Instructions, Game and MainMenu are childs of BaseClass.
# this is done so as to create modular code where we only need to change one
# template class to change the rest of the classes :) 

class BaseClass(tk.Tk): # BaseClass inherits from tk.Tk (part of built-in library)
    def __init__(self):
        tk.Tk.__init__(self) # initialisation = creating "starting template"

        self.title('SUTD Wordle') # title of pop-up in top left 

        self.refresh_mode() # this is to update darkmode colours

        self.font_used = "Inconsolata" # sets font for the other classes

        self.configure(bg=self.bg)
        self.geometry('800x800') # size of grid in pixels (not full screen)
        self.iconbitmap('img/favicon.ico') # icon of pop-up in top left 

        # Full Screen
        self.fullScreenState = True # default full screen
        try:
            # The code for the fullscreen function was taken from the code found at 
            # https://www.delftstack.com/howto/python-tkinter/how-to-create-full-screen-window-in-tkinter/ 
            self.attributes('-fullscreen', self.fullScreenState)
            # self.bind binds keyboard events to action
            self.bind('<F11>', lambda event: self.attributes(
                '-fullscreen', not self.attributes('-fullscreen')))
            self.bind('<Escape>', lambda event: self.attributes(
                '-fullscreen', False))
        except:
            pass

    def refresh_mode(self):
        f = open('darkmode.txt','r')
        darkmode = f.read()
        f.close()

        # code basically sets the colours for the buttons/background/foreground
        if darkmode == 'False':
            self.bg = 'white'
            self.fg = 'black'
            self.green = '#64B56C'
            self.yellow = '#F6C550'
            self.gray = '#B7B7B7'
        else:
            self.bg = 'black'
            self.fg = 'white'
            self.green = '#E6725E'
            self.yellow = '#6FD0D7'
            self.gray = '#A5A5A5'