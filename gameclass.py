# import modules needed
import random
import config
import mainmenu
import tkinter as tk
from tkinter import messagebox

# initialising game
class Game(config.BaseClass):
    def __init__(self):
        config.BaseClass.__init__(self)

        self.main_frame = tk.Frame(self, bg=self.bg, height=1000, width=1500) # creating the space for individual boxes

        self.bind('<Key>',self.key_pressed) # binds any key on keyboard to function key_pressed

        label = tk.Label(self, text='\nW O R D L E', font=(
            self.font_used, 40), width=20, bg=self.bg, fg=self.fg)
        label.pack(pady=30)

        self.start_game()
        self.main_frame.pack(side='bottom')
        self.main_frame.pack_propagate(0) 

        self.mainloop() # ensures continuity of code
        
    def clear_window(self): # clear all boxes, i.e. restart game
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()

    def read_file(self):
        data = []
        f = open('five.txt','r') 
        for line in f:
            data.append(line.strip())
        return data # reads every word from five.txt & returns as an array (i.e. list [])

    def start_game(self):
        self.clear_window() # for second game onwards (new game)
        self.guess = '' # no guesses 
        self.letters = []
        self.letter_count = 0

        self.words = self.read_file()
            # reads list of words
        self.word = random.choice(self.words).upper()
            # selects random word
        print(self.word)

        self.generate_elements() # creates 30 empty boxes
        self.main_frame.pack(side='bottom')
        self.main_frame.pack_propagate(0)

# once gameplay starts
    def key_pressed(self,event): # event is keyboard is pressed: letter, backspace, or enter only
        if event.char >= 'a' and event.char <= 'z' or event.char >= 'A' and \
                event.char <= 'Z' or event.keysym in 'BackSpace/Return':
            if event.keysym == 'BackSpace':
                # prevent backspacing previous row
                if self.letter_count > 0 and (self.letter_count % 5 != 0 or self.letters[self.letter_count-1]['bg'] == self.bg):
                    self.letters[self.letter_count-1]['text'] = ' ' # empty button
                    self.letters[self.letter_count-3].focus() # focus on previous "not backspaced" box
                    self.guess = self.guess[:-1] # backspace by one element
                    self.letter_count -= 1

# submitting guess
            # checking 5 letters, click 'enter' key, background white, have >1 letter
            elif self.letter_count % 5 == 0 and event.keysym == 'Return' and \
                    self.letters[self.letter_count-1]['bg'] == self.bg and self.letter_count>0:
                # checking if guess is valid (part of words in five.txt)
                if self.guess.lower() in self.words:
                    if self.letter_count == 30:
                        self.check_word(self.guess,last=True)
                        self.guess = ''
                    else:
                        self.check_word(self.guess)
                        self.guess = '' # new guess after valid guess
                # if guess is invalid
                else:
                    self.letter_count -= 5
                    self.go_again()
                    self.guess = '' # empties current row
            
            # ensures 'enter' and 'backspace' keys cannot be used as part of guess e.g. hell_
            elif event.keysym == 'Return' or event.keysym == 'BackSpace':
                pass

            # check 1. letters < 30 and 2. (nothing written or <5 letters) OR 3. (<5 letters or background not white)
            # first check to continue to next guess, second check to restrict guess to 5 letters for submission, third check allows new guess after submission
            elif self.letter_count <= 29 and ((self.letter_count % 5 != 0 or self.letter_count == 0) or \
                                (self.letter_count % 5 != 0 or self.letters[self.letter_count-1]['bg'] != self.bg)):
                self.letters[self.letter_count]['text'] = event.char.upper() # set button to letter typed
                self.letters[self.letter_count].focus()
                self.guess = self.guess + event.char.upper() # add letter typed to guess
                self.letter_count += 1

    def win_lose(self,winner):
        # pop-up text for win/lose, ask to play again or quit w/ respective pop-ups
        if not winner:
            title = 'you lose'
            message = f'The word was {self.word}'
        else:
            title = 'you win'
            message = 'well done, you got it in {} guess(s)'.format(int(self.letter_count / 5))
        play_again = messagebox.askquestion(title=title, message=f'{message}.\nwould you like to play again?')
        if play_again == 'yes':
            self.start_game()
        else:
            self.credit_window()
    
    # if guess is invalid, guess deleted
    def go_again(self):
        for i in range(5):
            self.letters[self.letter_count + i]['text'] = ' '

    # check guess to actual answer (when guess is valid)
    def check_word(self,guess,last=False):
        btn_index = self.letter_count - 5
        wrong_pos_check = False #check for guess with 1 yellow but answer has 2 of that letter 
        for i, letter in enumerate(guess):
            if letter == self.word[i]:
                self.letters[btn_index + i]['bg'] = self.green # background for correct letter
                self.letters[btn_index + i]['activebackground'] = self.green
            elif letter in self.word: 
                if guess.count(letter) >= 1 and guess.count(letter) == self.word.count(letter):
                    self.letters[btn_index + i]['bg'] = self.yellow
                    self.letters[btn_index + i]['activebackground'] = self.yellow
                elif not wrong_pos_check:
                    wrong_pos_check = True
                    self.letters[btn_index + i]['bg'] = self.yellow
                    self.letters[btn_index + i]['activebackground'] = self.yellow
                else:
                    self.letters[btn_index + i]['bg'] = self.gray
                    self.letters[btn_index + i]['activebackground'] = self.gray
            else:
                self.letters[btn_index + i]['bg'] = self.gray
                self.letters[btn_index + i]['activebackground'] = self.gray
        if guess == self.word: # if guess is correct, go to win function
            self.win_lose(True) 
        else:
            if last:
                self.win_lose(False)

    def generate_elements(self): # creates 6x5 grid of boxes
        self.gridframe = tk.Frame(self.main_frame)
        self.gridframe.pack(expand=True)

        for row in range(6): # 6 rows
            for col in range(5): # 5 columns
                # creates one box 
                btn = tk.Button(self.gridframe, text=' ',
                                width=3,height=0,font=(self.font_used,35),
                                bg=self.bg, fg=self.fg, activebackground=self.bg)
                btn.grid(row=row, column=col, padx=3, pady=3) 
                self.letters.append(btn) # put button into list (there will be 30 buttons)

    def credit_window(self):
        self.destroy()
        mainmenu.MainMenu()