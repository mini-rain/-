import pygame
from random import randint

# 定义常量
empty = 0
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
background = pygame.image.load("F:\\GitHub\\Tic_tac_toe\\TicTacToe.jpg")

# 棋盘状态
state = [[empty] * 3 for _ in range(3)]


def draw_game(screen, background):
    screen.blit(background, (0, 0))

    # 画线
    for x in [160, 320]:
        pygame.draw.line(screen, black, (x, 0), (x, 480), 5)
    for y in [160, 320]:
        pygame.draw.line(screen, black, (0, y), (480, y), 5)

    # 绘制棋子
    for row, line in enumerate(state):
        for col, val in enumerate(line):
            if val == -1:  # 'X'
                pygame.draw.line(screen, red, (col * 160 + 30, row * 160 + 30),
                                 (col * 160 + 130, row * 160 + 130), 5)
                pygame.draw.line(screen, red, (col * 160 + 130, row * 160 + 30),
                                 (col * 160 + 30, row * 160 + 130), 5)
            elif val == 1:  # 'O'
                pygame.draw.ellipse(screen, blue,
                                    (col * 160 + 25, row * 160 + 25, 110, 110), 5)

    pygame.display.flip()


def draw_O():
    while True:
        row = randint(0, 2)
        col = randint(0, 2)
        if state[row][col] == empty:
            state[row][col] = 1
            break


def begin(screen):
    global state
    state = [[empty] * 3 for _ in range(3)]
    draw_game(screen,background)
