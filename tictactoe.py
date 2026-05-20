import tkinter as tk 
from tkinter import messagebox

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic Tac Toe")

        self.human = "X"
        self.ai = "O"
        self.board = [""] * 9
        self.buttons = []
        
        self.create_buttons()

    def create_buttons(self):       

        for index in range(len(self.board)):
            button = tk.Button(
                self.window,
                text="",
                font=("Arial", 30),
                width=5,
                height=2,
                command=lambda index=index: self.button_clicked(index)
            )
            row_count = index // 3
            column_count = index % 3            
            button.grid(row=row_count + 1, column=column_count)
            self.buttons.append(button)

    def button_clicked(self,index):
        if self.board[index] == "":
            self.board[index] = self.human
            self.buttons[index].config(text=self.human) 

            # Check For winner
            if self.check_winner(self.human):
                messagebox.showinfo("Game Over", f"Player {self.human} wins!")
                self.reset_game()
                return

            if "" not in self.board:
                messagebox.showinfo("Game Over", "It is a tie!")
                self.reset_game()
                return

            self.ai_move()

            if self.check_winner(self.ai):
                messagebox.showinfo("Game Over", f"Player {self.ai} wins!")
                self.reset_game()
                return

            if "" not in self.board:
                messagebox.showinfo("Game Over", "It is a tie!")
                self.reset_game()
                return

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_winner(self, player):
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] == player:
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

    def ai_move(self):
        best_score = -999
        best_move = None

        for index in range(len(self.board)):
            if self.board[index] == "":
                self.board[index] = self.ai
                score = self.minimax(False)
                self.board[index] = ""

                if score > best_score:
                    best_score = score
                    best_move = index
        if best_move is not None:
            self.board[best_move] = self.ai
            self.buttons[best_move].config(text=self.ai)

    def minimax(self, is_ai_turn):
        if self.check_winner(self.ai):
            return 1

        if self.check_winner(self.human):
            return -1

        if "" not in self.board:
            return 0

        if is_ai_turn:
            best_score = -999
            for index in range(len(self.board)):
                if self.board[index] == "":
                    self.board[index] = self.ai
                    print(f"Ai turn : {self.board}")
                    score = self.minimax(False)
                    self.board[index] = ""
                    best_score = max(best_score, score)

            return best_score
        else:
            best_score = 999
            for index in range(len(self.board)):
                if self.board[index] == "":
                    self.board[index] = self.human
                    print(f"Human turn : {self.board}")
                    score = self.minimax(True)
                    self.board[index] = ""
                    best_score = min(best_score, score)

            return best_score


def main():
    window = tk.Tk()
    game = TicTacToe(window)
    window.mainloop()

if __name__ == "__main__":
    main()