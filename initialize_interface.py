import tkinter as tk
import winsound  # 用于播放音效（仅适用于 Windows）

class TicTacToeInterface:
    def __init__(self, master, mode_change_callback):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

          #双人模式与AI模式选择
        self.ai_enabled = False  # 默认是双人对战模式
        self.mode_change_callback = mode_change_callback  # 存储回调函数
        self.create_mode_buttons()  # 创建模式选择按钮

          #AI难度选择
        self.difficulty = tk.StringVar(value="easy")  # 默认难度
        self.create_difficulty_selector()  # 创建难度选择菜单

        self.player_input = None  # 玩家输入逻辑，将在模式选择时初始化

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

    def create_mode_buttons(self):
        """创建游戏模式选择按钮"""
        #双人模式
        two_player_button = tk.Button(self.master, text="双人模式", font='Arial 14',
                                      command=self.start_two_player_mode)
        two_player_button.grid(row=9, column=0, columnspan=3)

        #AI模式
        ai_mode_button = tk.Button(self.master, text="AI模式", font='Arial 14',
                                   command=self.start_ai_mode)
        ai_mode_button.grid(row=18, column=0, columnspan=3)

    def start_two_player_mode(self):
        """开始双人对战模式"""
        self.reset_board()  # 重置游戏
        self.ai_enabled = False  # 设置为双人对战模式
        self.start_game()  # 启动游戏

    def start_ai_mode(self):
        """开始 AI 对战模式"""
        self.reset_board()  # 重置游戏
        self.ai_enabled = True  # 设置为 AI 对战模式
        self.start_game()  # 启动游戏

    def start_game(self):
        """启动游戏并传递 ai_enabled 状态"""
        from player_input import PlayerInput
        if self.player_input is not None:
            self.player_input.reset_game()  # 如果已有实例，重置当前游戏
        self.player_input = PlayerInput(self, ai_enabled=self.ai_enabled)  # 将当前模式传递给 PlayerInput
        self.on_click = self.player_input.handle_click  # 更新点击事件绑定

    def reset_board(self):
        """重置棋盘按钮"""
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', bg="SystemButtonFace", state="normal")

        # 清除结果标签和重玩按钮
        for widget in self.master.grid_slaves():
            if int(widget.grid_info()["row"]) in [3, 4, 5]:
                widget.grid_forget()