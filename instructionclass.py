# import modules needed
import config
import mainmenu
import tkinter as tk

# write the new window function which
# will be called when button pressed

text1 = '\n\n\nhow to play Wordle!\n\nguess the wordle within 6 tries\neach guess must be a valid 5-letter word\
        \nthe colour of the tiles will change to show how close your guess was to the word\n\n'
text2 =  'H is in the word and in the correct spot\n\n'
text3 = 'O is in the word but is in the wrong spot\n\n'
text4 = 'E is not in the word and not in any spot\n\n'
        
# initialised the same way as main menu
class Instructions(config.BaseClass):
    def __init__(self):
        config.BaseClass.__init__(self)

        self.buttons = []

        self.answer_label = tk.Label(self, text=text1, bg=self.bg, fg=self.fg, font=(
            self.font_used, 20))
        self.answer_label.pack(pady=0)

        self.gridframe1 = tk.Frame(self, bg=self.bg, height=0, width=10)
        self.row_buttons('HELLO',self.gridframe1)
        self.gridframe1.pack(side='top')
        self.gridframe1.pack_propagate(0) 

        self.buttons[0]['bg'] = self.green # these set the tile colour for the highlighted letters for instructions
        self.buttons[0]['activebackground'] = self.green

        self.answer_label = tk.Label(self, text=text2, bg=self.bg, fg=self.fg, font=(
            self.font_used, 20))
        self.answer_label.pack(pady=0)

        self.gridframe2 = tk.Frame(self, bg=self.bg, height=0, width=10)
        self.row_buttons('WORLD',self.gridframe2)
        self.gridframe2.pack()
        self.gridframe2.pack_propagate(0) 

        self.buttons[6]['bg'] = self.yellow # these set the tile colour for the highlighted letters for instructions
        self.buttons[6]['activebackground'] = self.yellow

        self.answer_label = tk.Label(self, text=text3, bg=self.bg, fg=self.fg, font=(
            self.font_used, 20))
        self.answer_label.pack(pady=0)

        self.gridframe3 = tk.Frame(self, bg=self.bg, height=0, width=10)
        self.row_buttons('CODER',self.gridframe3)
        self.gridframe3.pack()
        self.gridframe3.pack_propagate(0) 

        self.buttons[13]['bg'] = self.gray # these set the tile colour for the highlighted letters for instructions
        self.buttons[13]['activebackground'] = self.gray

        self.answer_label = tk.Label(self, text=text4, bg=self.bg, fg=self.fg, font=(
            self.font_used, 20))
        self.answer_label.pack(pady=0)

        quit_button = tk.Button(self, text="go back", font=(
            self.font_used, 30), bg=self.bg, fg=self.fg,
            command=self.go_back)
        quit_button.pack(pady=0)

    def row_buttons(self,word,gf):
        for col in range(5):
                btn = tk.Button(gf, text=word[col],
                                width=3,height=0,font=(self.font_used,35),
                                bg=self.bg, fg=self.fg, activebackground=self.bg)
                btn.grid(row=0,column=col, padx=3, pady=0) 
                self.buttons.append(btn)

    def go_back(self):
        self.destroy()
        mainmenu.MainMenu() # goes back to main menu after quitting





