import tkinter as tk
import winsound  # 用于播放音效（仅适用于 Windows）

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
                                                command=lambda row=i, col=j: self.animate_button(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def animate_button(self, row, col):
        button = self.buttons[row][col]
        if button['text'] == '':
            button.config(bg="lightblue")  # 按下时改变背景色
            self.master.after(100, lambda: button.config(bg="SystemButtonFace"))  # 延迟后恢复原色
            winsound.PlaySound("click.wav", winsound.SND_ASYNC)  # 播放音效（需要准备 click.wav 文件）
            # 在 PlayerInput 中处理点击事件
            if hasattr(self, "on_click"):
                self.on_click(row, col)

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', bg="SystemButtonFace")
