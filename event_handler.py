from tkinter import messagebox
from check import check_winner
import pygame
from board import draw_game, draw_O, state,begin

background = pygame.image.load("F:\\GitHub\\Tic_tac_toe\\TicTacToe.jpg")
def handle_events(event, screen):
    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:  # 重启游戏
            begin(screen)
        elif event.key == pygame.K_s:  # 退出游戏
            pygame.quit()
            exit(0)

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        row, col = divmod(event.pos[1], 160)[0], divmod(event.pos[0], 160)[0]
        if state[int(row)][int(col)] == 0:  # 假设0表示空格
            state[int(row)][int(col)] = -1
            draw_game(screen,background)  # 重新绘制游戏
            draw_O()  # 在合适的位置绘制O

            # 这里检查获胜条件
            winner =check_winner(state)
            if winner == -1:
                messagebox.showinfo(title='Win', message='You win!')
                pygame.quit()
                exit(0)
            elif winner == 1:
                messagebox.showinfo(title='Lose', message='You lose!')
                pygame.quit()
                exit(0)
