import random
from check import GameCheck # 导入检查胜负的函数

class AI:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def make_move(self, board):
        if self.difficulty == 'easy':
            return self.random_move(board)
        elif self.difficulty == 'medium':
            return self.medium_move(board)
        elif self.difficulty == 'hard':
            return self.minimax_move(board)

    def random_move(self, board):
        empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == '']
        return random.choice(empty_cells) if empty_cells else None

    def medium_move(self, board):
        # 尝试阻止对手获胜
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = 'O'
                    if GameCheck(board) == 'O':
                        return (row, col)
                    board[row][col] = ''
        return self.random_move(board)

    def minimax_move(self, board):
        best_score = float('-inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = 'O'
                    score = self.minimax(board, False)
                    board[row][col] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move

    def minimax(self, board, is_maximizing):
        winner = GameCheck(board)
        if winner == 'O':
            return 1
        elif winner == 'X':
            return -1
        elif winner == 'draw':
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = 'O'
                        score = self.minimax(board, False)
                        board[row][col] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = 'X'
                        score = self.minimax(board, True)
                        board[row][col] = ''
                        best_score = min(score, best_score)
            return best_score
