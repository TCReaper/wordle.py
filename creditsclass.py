# import modules needed
import config
import tkinter as tk

# write the new window function which
# will be called when button pressed

thanks = "\n\n\nthanks for playing my game!\n\ncode by reaPYre"

class Credits(config.BaseClass):
    def __init__(self): 
        config.BaseClass.__init__(self)

        self.answer_label = tk.Label(self, text=thanks, bg=self.bg, fg=self.fg,
                                        font=(self.font_used, 30))
        self.answer_label.pack(pady=30)

        quit_button = tk.Button(self, text="quit", font=(
            self.font_used, 30), bg=self.bg, fg=self.fg,
            command=self.destroying)
        quit_button.pack(pady=30)

    def destroying(self):
        self.destroy() # nothing called since game quit





