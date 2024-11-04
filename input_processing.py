import pygame
from random import randint
import tkinter.messagebox as messagebox
from pygame.locals import *

# 初始化游戏
pygame.init()
width, height = 480, 480

# 创建屏幕并保存到变量中
screen = pygame.display.set_mode((width, height))

# 标题
pygame.display.set_caption("井字棋")

# 插入图片
try:
    background = pygame.image.load("C:/Users/王世伟/PycharmProjects/pythonProject1/bjt.png")
except FileNotFoundError:
    print("背景图片未找到，请确保图片位于正确位置或提供正确的路径。")
    exit(1)

# 定义常量
empty = 0
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# 棋盘状态
state = [[empty] * 3 for _ in range(3)]


# 创建绘制棋盘的函数
def draw_game():
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


# 随机在空位置放置'O'
def draw_O():
    while True:
        row = randint(0, 2)
        col = randint(0, 2)
        if state[row][col] == empty:
            state[row][col] = 1
            break
    draw_game()


# 检查是否获胜
def is_won():
    for val in range(3):
        # 检查行
        if all(state[row][val] == state[row + 1][val] == state[row + 2][val] != empty
               for row in range(3)):
            return state[0][val]

            # 检查列
        if all(state[val][row] == state[val][row + 1] == state[val][row + 2] != empty
               for row in range(3)):
            return state[val][0]

            # 检查对角线
    if all(state[i][i] == state[i + 1][i + 1] == state[i + 2][i + 2] != empty
           for i in range(3)):
        return state[1][1]
    if all(state[i][2 - i] == state[i + 1][1 - i] == state[i + 2][0 - i] != empty
           for i in range(3)):
        return state[1][1]

    return None


# 初始化棋盘并开始游戏
def begin():
    global state
    state = [[empty] * 3 for _ in range(3)]
    draw_game()


begin()

# 主循环
while True:
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)

    elif event.type == KEYDOWN:
        if event.key == pygame.K_a:  # 使用pygame.K_A确保一致性
            begin()
        elif event.key == pygame.K_s:  # 使用pygame.K_S确保一致性
            pygame.quit()
            exit(0)

    elif event.type == MOUSEBUTTONDOWN and event.button == 1:
        row, col = divmod(event.pos[1], 160)[0], divmod(event.pos[0], 160)[0]
        if state[int(row)][int(col)] == empty:
            state[int(row)][int(col)] = -1
            draw_game()
            draw_O()

            # 判断获胜者
            winner = is_won()
            if winner == -1:
                messagebox.showinfo(title='Win', message='You win!')
                pygame.quit()
                exit(0)
            elif winner == 1:
                messagebox.showinfo(title='Lose', message='You lose!')
                pygame.quit()
                exit(0)
