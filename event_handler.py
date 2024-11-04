import pygame
import tkinter.messagebox as messagebox
from check import check_winner
from board import draw_game, draw_O, state, begin


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

            # 检查获胜条件
            winner = check_winner(state)
            if winner == -1:
                messagebox.showinfo(title='Win', message='You win!')
                pygame.quit()
                exit(0)
            elif winner == 1:
                messagebox.showinfo(title='Lose', message='You lose!')
                pygame.quit()
                exit(0)

            # 让计算机进行下一步
            draw_O()  # 计算机放置"O"
            draw_game(screen, background)  # 更新游戏界面

            # 再次检查获胜条件
            winner = check_winner(state)
            if winner == -1:
                messagebox.showinfo(title='Win', message='You win!')
                pygame.quit()
                exit(0)
            elif winner == 1:
                messagebox.showinfo(title='Lose', message='You lose!')
                pygame.quit()
                exit(0)
