import tkinter as tk

class TicTacToe:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")

        # Create the game board
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        self.start_game()

    def start_game(self):
        # Create the buttons for the game board
        self.buttons = []
        for i in range(3):
            button_row = []
            for j in range(3):
                button = tk.Button(self.frame, text=" ", width=10, height=5,
                                command=lambda r=i, c=j: self.button_clicked(r, c))
                button.grid(row=i, column=j)
                button_row.append(button)
            self.buttons.append(button_row)

        print(self.buttons)

        # Create a label to display the current player's turn
        self.turn_label = tk.Label(self.root, text="Player X's turn")
        self.turn_label.grid(row=1, column=0)

        # Create a label to display the winner (if any)
        self.winner_label = tk.Label(self.root, text="                              ")
        self.winner_label.grid(row=2, column=0)

        # Create a button to start a new game
        self.new_game_button = tk.Button(self.frame, text="New Game",
                                        command=lambda : self.start_game())
        self.new_game_button.grid(row=4, column=1, sticky="ew")

        # Initialize the game state
        self.player = "X"
        self.winner = None

    def button_clicked(self, row, column):
        # Check if the game is already over
        if self.winner is not None:
            return

        # Check if the selected square is empty
        if self.buttons[row][column]["text"] != " ":
            return

        # Place the player's symbol on the selected square
        self.buttons[row][column]["text"] = self.player

        # Check if the player has won
        if self.check_winner():
            self.winner_label["text"] = f"Player {self.player} wins!"
            self.winner = self.player

        # Switch to the other player's turn
        if self.player == "X":
            self.player = "O"
            self.turn_label["text"] = "Player O's turn"
        else:
            self.player = "X"
            self.turn_label["text"] = "Player X's turn"

    def check_winner(self):
        # Check for a horizontal win
        for row in self.buttons:
            if row[0]["text"] == row[1]["text"] == row[2]["text"] != " ":
                return True

        # Check for a vertical win
        for column in range(3):
            if self.buttons[0][column]["text"] == self.buttons[1][column]["text"] == self.buttons[2][column]["text"] != " ":
                return True

        # Check for a diagonal win
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != " ":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != " ":
            return True

        # If no win is found, return False
        return False

    def play_game(self):
        self.root.mainloop()

def main():
    ttt = TicTacToe()
    ttt.play_game()

if __name__ == "__main__":
   main()
