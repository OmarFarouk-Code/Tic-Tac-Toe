import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        # --- Data Initialization ---
        self.x_score = 0 
        self.o_score = 0
        self.current_player = "X"
        
        # --- Window Setup ---
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe Pro")
        self.window.geometry("450x550")
        self.window.configure(bg="#f0f0f0") # Light grey background

        # --- UI Elements ---
        # Score Display
        self.label = tk.Label(
            self.window, 
            text=f"X Score: {self.x_score}  |  O Score: {self.o_score}", 
            font=("Helvetica", 16, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        # 3. Restart Button (The New Feature)
        self.restart_btn = tk.Button(
            self.window,
            text="Restart Full Game",
            font=("Arial", 12, "bold"),
            bg="#333333",
            fg="white",
            activebackground="#555555",
            activeforeground="white",
            command=self.restart_full_game,
            padx=20,
            pady=10)
        
        self.restart_btn.pack(pady=20)
        self.label.pack(pady=20)

        # Game Board Container
        self.frame = tk.Frame(self.window, bg="#333333", bd=2) # Dark border for grid
        self.frame.pack(expand=True)

        self.create_buttons()

        
    
    def run(self):
        #Starts the Tkinter event loop.
        self.window.mainloop()

    def create_buttons(self):
        #Generates the 3x3 grid of interactive buttons.
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    self.frame, 
                    text="", 
                    font=("Arial", 24, "bold"), 
                    width=5, 
                    height=2,
                    relief="flat",          # Flatter, modern look
                    bg="white",
                    activebackground="#e1e1e1", # Visual feedback on click
                    command=lambda i=i, j=j: self.handle_click(i, j)
                )
                button.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
                row.append(button)
            self.buttons.append(row)

    def handle_click(self, i, j):
        #Logic for when a player clicks a square.
        # 1. Check if the move is valid (cell is empty)
        
        if self.buttons[i][j]["text"] == "":
            
            # 2. Place mark and style based on current player
            color = "#2196F3" if self.current_player == "X" else "#F44336" # Blue for X, Red for O
            self.buttons[i][j].config(text=self.current_player, fg=color)
            
            # 3. Check if this move won the game
            if self.check_for_winner():
                winner = self.buttons[i][j]["text"]
                messagebox.showinfo("Game Over", f"🌟 Player {winner} Wins! 🌟")
                self.update_score(winner)
                self.reset_game()
            
            # 4. Check if the board is full (Draw)
            elif self.check_for_draw():
                messagebox.showinfo("Game Over", "🤝 It's a Draw! 🤝")
                self.reset_game()
            
            # 5. Switch turn if game continues
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Invalid Move", "That spot is taken!")

    def check_for_winner(self):
        #Checks rows, columns, and diagonals for 3 matching symbols.
        # Check Rows
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                self.highlight_winner([self.buttons[i][0], self.buttons[i][1], self.buttons[i][2]])
                return True
        
        # Check Columns
        for j in range(3):
            if self.buttons[0][j]["text"] == self.buttons[1][j]["text"] == self.buttons[2][j]["text"] != "":
                self.highlight_winner([self.buttons[0][j], self.buttons[1][j], self.buttons[2][j]])
                return True
        
        # Check Diagonals
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            self.highlight_winner([self.buttons[0][0], self.buttons[1][1], self.buttons[2][2]])
            return True
        
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            self.highlight_winner([self.buttons[0][2], self.buttons[1][1], self.buttons[2][0]])
            return True

        return False

    def highlight_winner(self, winning_buttons):
        #Changes the background color of winning buttons.
        for btn in winning_buttons:
            btn.config(bg="#4CAF50", fg="white") # Material Design Green

    def check_for_draw(self):
        #Returns True if no empty cells remain.
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]["text"] == "":
                    return False
        return True

    def reset_game(self):
        #Clears the board and resets current player to X.
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", bg="white")
        self.current_player = "X"

    def update_score(self, winner):
        #Increments the winner's score and updates the UI label.
        if winner == "X":
            self.x_score += 1
        else:
            self.o_score += 1
        self.label.config(text=f"X Score: {self.x_score}  |  O Score: {self.o_score}")

    def restart_full_game(self):
        # 1. Ask for confirmation so points aren't lost by accident
        confirm = messagebox.askyesno("Confirm Restart", "Reset all scores and the board?")
        
        if confirm:
            # 2. Reset the data variables
            self.x_score = 0
            self.o_score = 0
            self.current_player = "X"
            
            # 3. Update the visual Label
            self.label.config(text=f"X Score: {self.x_score}  |  O Score: {self.o_score}")
            
            # 4. Clear the board using the method we already wrote
            self.reset_game()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()