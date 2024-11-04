import tkinter as tk
from initialize_interface import TicTacToeInterface
from player_input import PlayerInput

def main():
    root = tk.Tk()
    interface = TicTacToeInterface(root)
    player_input = PlayerInput(interface)

    for i in range(3):
        for j in range(3):
            interface.buttons[i][j].config(command=lambda row=i, col=j: player_input.handle_click(row, col))

    root.mainloop()

if __name__ == "__main__":
    main()
