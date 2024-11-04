# check.py

def check_winner(state):
    # 检查行
    for row in state:
        if row[0] == row[1] == row[2] != 0:
            return row[0]

    # 检查列
    for col in range(3):
        if state[0][col] == state[1][col] == state[2][col] != 0:
            return state[0][col]

    # 检查对角线
    if state[0][0] == state[1][1] == state[2][2] != 0:
        return state[0][0]
    if state[0][2] == state[1][1] == state[2][0] != 0:
        return state[2][0]

    # 检查平局
    if all(cell != 0 for row in state for cell in row):
        return 'draw'

    return None
