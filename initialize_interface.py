import tkinter as tk
import winsound  # 用于播放音效（仅适用于 Windows）


class TicTacToeInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        self.difficulty = tk.StringVar(value="easy")  # 默认难度
        self.create_difficulty_selector()  # 创建难度选择菜单

    def create_board(self):
        """创建 3x3 的棋盘按钮"""
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text='', font='Arial 20', width=5, height=2,
                                               command=lambda row=i, col=j: self.animate_button(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def animate_button(self, row, col):
        """按钮点击后进行动画效果和音效播放"""
        button = self.buttons[row][col]
        if button['text'] == '':  # 仅在空格子点击时有效
            button.config(bg="lightblue")  # 改变按钮背景颜色
            self.master.after(100, lambda: button.config(bg="SystemButtonFace"))  # 延时恢复颜色

            # 播放点击音效
            winsound.PlaySound("click.wav", winsound.SND_ASYNC)

            # 调用外部点击处理逻辑
            if hasattr(self, "on_click"):
                self.on_click(row, col)

    def create_difficulty_selector(self):
        """创建难度选择菜单"""
        difficulty_label = tk.Label(self.master, text="Select Difficulty:", font='Arial 12')
        difficulty_label.grid(row=7, column=0, columnspan=3, sticky="w")

        difficulties = ["easy", "medium", "hard"]
        difficulty_menu = tk.OptionMenu(self.master, self.difficulty, *difficulties)
        difficulty_menu.grid(row=8, column=0, columnspan=3, sticky="w")

    def reset_board(self):
        """重置棋盘按钮"""
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', bg="SystemButtonFace", state="normal")
