class GameCheck:
    def __init__(self, buttons):
        # 将按钮的文本状态提取为二维数组，方便检查
        self.state = [[buttons[i][j]['text'] for j in range(3)] for i in range(3)]

    def evaluate_game(self):
        # 检查行
        for row in self.state:
            if row[0] == row[1] == row[2] != '':
                return row[0]  # 返回获胜者 "X" 或 "O"

        # 检查列
        for col in range(3):
            if self.state[0][col] == self.state[1][col] == self.state[2][col] != '':
                return self.state[0][col]

        # 检查对角线
        if self.state[0][0] == self.state[1][1] == self.state[2][2] != '':
            return self.state[0][0]
        if self.state[0][2] == self.state[1][1] == self.state[2][0] != '':
            return self.state[2][0]

        # 检查平局
        if all(cell != '' for row in self.state for cell in row):
            return 'draw'

        return None
