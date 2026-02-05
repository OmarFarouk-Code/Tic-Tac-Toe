import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__ (self):

        self.x_score = 0 
        self.o_score = 0
        self.current_player = "X"
        self.window = tk.Tk()
        self.window.title ("Tic Tac Toe")
        self.window.geometry("400x400")

        self.frame = tk.Frame (self.window , width = 400 , height = 400)
        self.frame.pack()
        self.label = tk.Label(self.window , text = f"Player X Score: {self.x_score}\nPlayer O Score: {self.o_score}" , font = ("Arial", 14 , "bold") )
        self.label.pack(pady=10)
        self.create_buttons()
    
    def run (self):
        self.window.mainloop()

    def create_buttons (self):
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):

                button = tk.Button(self.frame , text = "" , command =  lambda i=i, j=j: self.handle_click(i, j) , font=("Arial", 24), width=5, height=2)
                self.frame.grid_rowconfigure(i, weight=1)
                self.frame.grid_columnconfigure(j, weight=1)
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)

            self.buttons.append(row)

    def handle_click (self, i, j):
        if self.buttons[i][j]["text"] == "":

            if self.current_player == "X":

                self.buttons[i][j].config(text=self.current_player , fg="blue")
                self.current_player = "O"
            else:
                self.buttons[i][j].config(text=self.current_player , fg="red")
                self.current_player = "X"
            
            if self.check_for_winner():
                
                winner = self.buttons[i][j]["text"]
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.update_score(winner)
                self.reset_game()

            elif self.check_for_draw():

                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()

        else :
            messagebox.showinfo("Invalid Move", "This cell is already occupied. Please choose another one." )


    def check_for_winner(self):
        #Check Rows
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":

                self.buttons[i][0].config(bg="Green")
                self.buttons[i][1].config(bg="Green")
                self.buttons[i][2].config(bg="Green")
               
                return True
        
        #Check Columns
        for j in range(3):
            if self.buttons[0][j]["text"] == self.buttons[1][j]["text"] == self.buttons[2][j]["text"] != "":

                self.buttons[0][j].config(bg="Green")
                self.buttons[1][j].config(bg="Green")
                self.buttons[2][j].config(bg="Green")
                
                return True
        
        #Check Diagonals
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":

            self.buttons[0][0].config(bg="Green")
            self.buttons[1][1].config(bg="Green")
            self.buttons[2][2].config(bg="Green")
            
            return True
        
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":

            self.buttons[0][2].config(bg="Green")
            self.buttons[1][1].config(bg="Green")
            self.buttons[2][0].config(bg="Green")
            
            return True

        return False

    def check_for_draw(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == "":
                    return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="" , bg = "White")
        self.current_player = "X"

    def update_score(self, winner):
        if winner == "X":
            self.x_score += 1
        elif winner == "O":
            self.o_score += 1
        
        # Update the label to show new totals
        self.label.config(text=f"Player X Score: {self.x_score}\nPlayer O Score: {self.o_score}")
        
        

if __name__ == "__main__":
    game = TicTacToe()
    game.run()