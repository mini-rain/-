# reset_game.py
import pandas as pd

# 初始化棋盘
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# 更新棋盘
def update_board(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

# 输出棋盘
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


