import tkinter as tk
from check import GameCheck
from AI_logic import AI
from score_tracker import ScoreTracker  # 导入 ScoreTracker


class PlayerInput:
    def __init__(self, interface, ai_enabled=False):
        self.interface = interface
        self.current_player = "X"
        self.ai_enabled = ai_enabled
        self.update_ai()  # 初始化 AI
        self.game_check = GameCheck(self.interface.buttons)
        self.score_tracker = ScoreTracker()  # 实例化 ScoreTracker
        self.create_score_display()  # 创建分数显示

    def create_score_display(self):
        """创建玩家得分显示"""
        self.score_label_x = tk.Label(self.interface.master, text="X Wins: 0 | Losses: 0 | Draws: 0", font='Arial 12')
        self.score_label_x.grid(row=5, column=0, columnspan=3, sticky="w")

        self.score_label_o = tk.Label(self.interface.master, text="O Wins: 0 | Losses: 0 | Draws: 0", font='Arial 12')
        self.score_label_o.grid(row=6, column=0, columnspan=3, sticky="w")

    def update_score_display(self):
        """从 ScoreTracker 更新玩家得分显示"""
        scores = self.score_tracker.scores
        x_score = scores["X"]
        o_score = scores["O"]

        self.score_label_x.config(
            text=f"X Wins: {x_score['win']} | Losses: {x_score['loss']} | Draws: {x_score['draw']}")
        self.score_label_o.config(
            text=f"O Wins: {o_score['win']} | Losses: {o_score['loss']} | Draws: {o_score['draw']}")

    def handle_click(self, row, col):
        button = self.interface.buttons[row][col]
        if button['text'] == '':
            button.config(text=self.current_player)
            self.process_turn(row, col)

            if self.ai_enabled and self.current_player == "O":
                self.handle_ai_turn()

    def handle_ai_turn(self):
        """调用 AI 获取下一步操作"""
        self.update_ai()  # 确保每次操作前更新难度
        row, col = self.ai.get_move(self.interface.buttons, "O", "X")
        self.interface.buttons[row][col].config(text="O")
        self.process_turn(row, col)

    def process_turn(self, row, col):
        """处理每轮游戏逻辑"""
        self.game_check.state = [[self.interface.buttons[i][j]['text'] for j in range(3)] for i in range(3)]
        result = self.game_check.evaluate_game()

        if result in ["X", "O", "draw"]:
            self.score_tracker.update_score(result)  # 更新分数记录
            self.end_game(f"{result} Wins!" if result != "draw" else "It's a Draw!")
        else:
            self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def end_game(self, message):
        """结束游戏并显示结果"""
        for row in range(3):
            for col in range(3):
                self.interface.buttons[row][col].config(state="disabled")

        result_label = tk.Label(self.interface.master, text=message, font='Arial 20')
        result_label.grid(row=3, columnspan=3)

        reset_button = tk.Button(self.interface.master, text="Play Again", command=self.reset_game)
        reset_button.grid(row=4, columnspan=3)

        self.update_score_display()  # 更新分数显示

    def reset_game(self):
        """重置游戏，保留分数记录"""
        self.interface.reset_board()
        self.current_player = "X"

        # 清除结果标签和重玩按钮
        for widget in self.interface.master.grid_slaves():
            if int(widget.grid_info()["row"]) in [3, 4]:  # 仅清除结果显示和重玩按钮
                widget.grid_forget()

        # 恢复按钮状态
        for row in range(3):
            for col in range(3):
                self.interface.buttons[row][col].config(state="normal")

        # 重新初始化 GameCheck
        self.game_check = GameCheck(self.interface.buttons)

    def update_ai(self):
        """根据界面上的难度设置更新 AI"""
        if self.ai_enabled:
            difficulty = self.interface.difficulty.get()
            self.ai = AI(difficulty)
        else:
            self.ai = None
