import tkinter as tk
from check import GameCheck  # 导入 GameCheck

class PlayerInput:
    def __init__(self, interface):
        self.interface = interface
        self.current_player = "X"
        self.game_check = GameCheck(self.interface.buttons)  # 实例化 GameCheck

    def handle_click(self, row, col):
        button = self.interface.buttons[row][col]
        if button['text'] == '':
            button.config(text=self.current_player)

            # 更新 game_check 的状态
            self.game_check.state = [[self.interface.buttons[i][j]['text'] for j in range(3)] for i in range(3)]
            result = self.game_check.evaluate_game()

            if result == "X" or result == "O":
                self.end_game(f"{result} Wins!")
            elif result == "draw":
                self.end_game("It's a Draw!")
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def end_game(self, message):
        for row in range(3):
            for col in range(3):
                self.interface.buttons[row][col].config(state="disabled")
        result_label = tk.Label(self.interface.master, text=message, font='Arial 20')
        result_label.grid(row=3, columnspan=3)

        reset_button = tk.Button(self.interface.master, text="Play Again", command=self.reset_game)
        reset_button.grid(row=4, columnspan=3)

    def reset_game(self):
        self.interface.reset_board()
        self.current_player = "X"

        # 清除结果标签和重玩按钮
        for widget in self.interface.master.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:
                widget.grid_forget()

        # 恢复棋盘按钮的状态为正常
        for row in range(3):
            for col in range(3):
                self.interface.buttons[row][col].config(state="normal")
