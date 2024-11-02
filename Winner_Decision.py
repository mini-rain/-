#导入库
import pandas as pd

#输入3*3的矩阵数据，标记行，列
data =[ ['x','x','o'],
        ['o','x','o'],
        ['x','o','o']
]

#胜负判定算法
def check_winner(data):
#按行遍历，遍历每一行
    for row in data:
        print(row[0],row[1],row[2])
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

        
    #按列遍历，遍历每一列
    for col in range(3):
        print(data[0][col],data[1][col],data[2][col])
        if data[0][col] == data[1][col] == data[2][col] != ' ':
            return data[2][col]

    #对角线检查，遍历对角线
    print(data[0][0],data[1][1],data[2][2])
    if data[0][0] == data[1][1] == data[2][2] != ' ':
        return data[0][0]
    print(data[0][2],data[1][1],data[2][0])
    if data[0][2] == data[1][1] == data[2][0] != ' ':
        return data[2][0]

    #平局检测
    if all(cell != ' ' for row in data for cell in row):
        return 'draw'
    
    return None
#输出比赛结果
result = check_winner(data)

if result == 'x':
    print("the winner is X")
elif result == 'o':
    print("the winner is O")
elif result == 'draw':
    print("nobody win, it's draw,Please select whether or not to continue the game ...")
else: 
    print("the gama is going")