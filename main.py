import tkinter as tk
from initialize_interface import TicTacToeInterface
from player_input import PlayerInput

def main():
    root = tk.Tk()
    interface = TicTacToeInterface(root)
    player_input = PlayerInput(interface, ai_enabled=True)  # 启用 AI

    # 将按钮点击事件绑定到 PlayerInput 的 handle_click 方法
    interface.on_click = player_input.handle_click

    root.mainloop()

if __name__ == "__main__":
    main()
