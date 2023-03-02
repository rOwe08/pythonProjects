import tkinter as tk
import tkinter.messagebox as messagebox
import random
import math

class TicTacToe(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Tic Tac Toe")

        self.choose_board_size()
        self.choose_mode()
        
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.player = "X"
        self.buttons = []
        self.centeri, self.centerj = math.floor(self.board_size/2), math.floor(self.board_size/2)

        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                button = tk.Button(self, text=" ", font=("Helvetica", 32), height=1, width=4, command=lambda row=i, col=j: self.play(row, col))
                button.grid(row=i, column=j)
                row.append(button) 
            self.buttons.append(row)

        self.play_again_button = tk.Button(self, text="Play Again", font=("Helvetica", 16), height=2, width=10, state="disabled", command=self.play_again)
        self.play_again_button.grid(row=self.centeri, column=self.board_size, columnspan=self.board_size)

    def choose_board_size(self):
        def on_ok():
            global board_size
            board_size = int(size_var.get())
            top.destroy()

        top = tk.Toplevel(self)
        top.title("Choose Board Size")
        tk.Label(top, text="Select the size of the board:").pack(padx=10, pady=10)
        size_var = tk.StringVar(value="3")
        tk.OptionMenu(top, size_var, *[str(i) for i in range(3, 10)]).pack(padx=10, pady=10)
        tk.Button(top, text="OK", command=on_ok).pack(padx=10, pady=10)

        top.grab_set()
        top.wait_window()
        self.board_size = board_size

    def choose_mode(self):
        def on_ok():
            global mode
            mode = int(mode_var.get())
            top.destroy()

        top = tk.Toplevel(self)
        top.title("Choose Mode")
        tk.Label(top, text="How much players? (1-vsPC, 2-PvP):").pack(padx=10, pady=10)
        mode_var = tk.StringVar(value="1")
        tk.OptionMenu(top, mode_var, 1, 2).pack(padx=10, pady=10)
        tk.Button(top, text="OK", command=on_ok).pack(padx=10, pady=10)

        top.grab_set()
        top.wait_window()
        self.mode = mode

    def play(self, row, col):
        if self.board[row][col] is None:

            self.board[row][col] = self.player
            button = self.buttons[row][col]
            button.configure(text=self.player, state="disabled")

            if self.check_win():
                self.show_win_message()

            elif self.check_tie():
                self.show_tie_message()
            
            else:
                if self.mode == 1:
                    self.pc_play()

                elif self.mode == 2:
                    if self.player == "X":
                        self.player = "O"
                    else:
                        self.player = "X"
        else:
            messagebox.showerror("Tic Tac Toe", "Invalid move")

    def pc_play(self):

        empty_cells = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i][j] is None]

        if self.board[self.centeri][self.centerj] is None:
            row, col = self.centeri, self.centerj 
        else:
            row, col = random.choice(empty_cells)

        self.player = "O"
        self.board[row][col] = self.player
        button = self.buttons[row][col]
        button.configure(text=self.player, state="disabled")
        
        if self.check_win():
            self.show_win_message()
        elif self.check_tie():
            self.show_tie_message()
        else:
            self.player = "X"

    def check_win(self):
        for row in range(self.board_size):
            if all(self.board[row][col] == self.player for col in range(self.board_size)):
                return True
            
        for col in range(self.board_size):
            if all(self.board[row][col] == self.player for row in range(self.board_size)):
                return True
            
        if all(self.board[i][i] == self.player for i in range(self.board_size)):
            return True
        if all(self.board[i][self.board_size - 1 - i] == self.player for i in range(self.board_size)):
            return True
        
        return False

    def check_tie(self):
        return all(cell is not None for row in self.board for cell in row)

    def show_win_message(self):
        messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
        self.play_again_button.configure(state="normal")

    def show_tie_message(self):
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        self.play_again_button.configure(state="normal")

    def play_again(self):
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.player = "X"
        self.play_again_button.configure(state="disabled")

        for row in self.buttons:
            for button in row:
                button.configure(text=" ", state="normal")

app = TicTacToe()
app.mainloop()


