import tkinter as tk

class TicTacToeInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text='', font='Arial 20', width=5, height=2,
                                                command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        pass  # 将在后续实现中添加点击处理逻辑

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
