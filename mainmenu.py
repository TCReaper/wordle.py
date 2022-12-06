# import modules
import config
import gameclass
import creditsclass
import tkinter as tk # built-in python library
import instructionclass

# write window function
padding = 30

class MainMenu(config.BaseClass): # MainMenu inherits from tk.Tk (part of built-in library)
    def __init__(self):
        config.BaseClass.__init__(self) # initialisation = creating "starting template"

        self.answer_label = tk.Label(self, text='\nwelcome to WORDLE!', font=(
            self.font_used, 40), width=20, bg=self.bg, fg=self.fg)
        self.answer_label.pack(pady=padding) # pack window with title (label) ^

        button = tk.Button(self, text='play', font=(
            self.font_used, 30),bg=self.bg, fg=self.fg,
            command=lambda: self.init_game()) # assign initialising function to button upon clicking it
        button.pack(pady=padding) # pack 'play' button to start game

        button = tk.Button(self, text='instructions', font=(
            self.font_used, 30), bg=self.bg, fg=self.fg,
            command=lambda: self.show_instructions())
        button.pack(pady=padding)

        f = open('darkmode.txt','r')
        darkmode = f.read()
        f.close()
        modetext = 'light mode' if darkmode=='True' else 'dark mode'

        button = tk.Button(self, text=f'{modetext}', font=(
            self.font_used, 30), bg=self.bg, fg=self.fg,
            command=lambda: self.change_mode(darkmode))
        button.pack(pady=padding)

        quit_button = tk.Button(self, text='quit', font=(
            self.font_used, 30), bg=self.bg, fg=self.fg,
            command=lambda: self.credit_window())
        quit_button.pack(pady=padding)
        self.mainloop()
        
    def show_instructions(self):
        self.destroy()
        instructionclass.Instructions()

    def change_mode(self,darkmode):
        if darkmode=='True':
            darkmode = 'False'
        else:
            darkmode = 'True'
            
        f = open('darkmode.txt','w')
        f.write(darkmode) # file overwriting to change the setting
        f.close()
        self.refresh_mode()
        self.destroy()
        MainMenu() # refresh page

    def credit_window(self):
        self.destroy()
        creditsclass.Credits()

    def init_game(self):
        self.destroy()
        gameclass.Game()

    # defining functions called 