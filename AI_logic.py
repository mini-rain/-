import random
from check import GameCheck  # 使用现有的 GameCheck 类

class AI:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty

    def get_move(self, buttons, ai_marker, human_marker):
        """
        根据难度选择 AI 的下一步
        :param buttons: 当前棋盘按钮（二维列表）
        :param ai_marker: AI 的标记 ("X" 或 "O")
        :param human_marker: 人类玩家的标记 ("X" 或 "O")
        :return: (row, col) 下一步的位置
        """
        # 使用 GameCheck 提取当前棋盘状态
        game_check = GameCheck(buttons)
        state = game_check.state

        if self.difficulty == "easy":
            return self.random_choice(state)
        elif self.difficulty == "medium":
            return self.rule_based_choice(state, ai_marker, human_marker, game_check)
        elif self.difficulty == "hard":
            return self.minimax(state, ai_marker, human_marker, game_check)["position"]

    def random_choice(self, state):
        """简单 AI：随机选择一个空格子"""
        empty_cells = [(row, col) for row in range(3) for col in range(3) if state[row][col] == ""]
        return random.choice(empty_cells)

    def rule_based_choice(self, state, ai_marker, human_marker, game_check):
        """中等难度 AI：优先选择获胜或阻止对方获胜的位置"""
        # 检查是否有获胜机会
        for row in range(3):
            for col in range(3):
                if state[row][col] == "":
                    state[row][col] = ai_marker
                    game_check.state = state
                    if game_check.evaluate_game() == ai_marker:
                        state[row][col] = ""
                        return (row, col)
                    state[row][col] = ""

        # 阻止玩家获胜
        for row in range(3):
            for col in range(3):
                if state[row][col] == "":
                    state[row][col] = human_marker
                    game_check.state = state
                    if game_check.evaluate_game() == human_marker:
                        state[row][col] = ""
                        return (row, col)
                    state[row][col] = ""

        # 如果没有直接威胁，则随机选择
        return self.random_choice(state)

    def minimax(self, state, ai_marker, human_marker, game_check, is_maximizing=True):
        """高级难度 AI：使用 Minimax 算法寻找最优解"""
        game_check.state = state
        winner = game_check.evaluate_game()

        if winner == ai_marker:
            return {"score": 10}
        elif winner == human_marker:
            return {"score": -10}
        elif winner == "draw":
            return {"score": 0}

        best_move = {"score": float('-inf') if is_maximizing else float('inf'), "position": None}

        for row in range(3):
            for col in range(3):
                if state[row][col] == "":
                    state[row][col] = ai_marker if is_maximizing else human_marker
                    score = self.minimax(state, ai_marker, human_marker, game_check, not is_maximizing)["score"]
                    state[row][col] = ""  # 还原

                    if is_maximizing:
                        if score > best_move["score"]:
                            best_move = {"score": score, "position": (row, col)}
                    else:
                        if score < best_move["score"]:
                            best_move = {"score": score, "position": (row, col)}

        return best_move