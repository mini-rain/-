import tkinter as tk
from initialize_interface import TicTacToeInterface
from player_input import PlayerInput

def main():
    root = tk.Tk()
    # # 默认选择双人对战模式
    ai_enabled = False
    # 创建界面并传递回调函数
    interface = TicTacToeInterface(root, None)

    # 创建 PlayerInput 对象
    player_input = PlayerInput(interface, ai_enabled)
    interface.on_click = player_input.handle_click  # 将点击事件绑定到 PlayerInput 的 handle_click 方法

    root.mainloop()

if __name__ == "__main__":
    main()
