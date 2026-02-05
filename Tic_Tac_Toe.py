import tkinter as tk

class TicTacToe:
    def __init__ (self):
        
        self.window = tk.Tk()
        self.window.title ("Tic Tac Toe")
        self.window.geomety("400x400")

        self.frame = tk.Frame (self.window)
        self.frame.pack()

        self.create_buttons()
    
    def run (self):
        self.window.mainloop()