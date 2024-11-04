import pygame
import tkinter.messagebox as messagebox
from board import draw_game, begin, state
from  event_handler import handle_events
import check

# 初始化游戏
pygame.init()
width, height = 480, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("井字棋")

# 插入图片
try:
    background = pygame.image.load("F:\\GitHub\\Tic_tac_toe\\TicTacToe.jpg")
except FileNotFoundError:
    print("背景图片未找到，请确保图片位于正确位置或提供正确的路径。")
    exit(1)

begin(screen)

# 主循环
while True:
    event = pygame.event.wait()
    handle_events(event, screen)

    # 判断获胜者
    winner = check.check_winner(state)
    if winner == -1:
        messagebox.showinfo(title='Win', message='You win!')
        pygame.quit()
        exit(0)
    elif winner == 1:
        messagebox.showinfo(title='Lose', message='You lose!')
        pygame.quit()
        exit(0)
