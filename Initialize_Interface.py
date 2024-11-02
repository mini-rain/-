import tkinter as tk

class GetBoard:
    def __init__(self, root, rows, cols):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cell_size = 100#每个单元格大小
        self.create_board() #创建画布
    
    #创建画布
    def create_board(self):
        self.canvas = tk.Canvas(self.root, width = self.cols * self.cell_size, height = self.rows * self.cell_size)
        self.canvas.pack()

        for row in range(self.rows):
            for col in range(self.cols):
                #横坐标
                x0 = col * self.cell_size 
                #纵坐标
                y0 = row * self.cell_size 
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0 , x1, y1, outline = "black", fill = "white")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("井字棋")

#创建3*3网格棋盘
get_board = GetBoard(root, 3, 3)               

root.mainloop()

#网格适配居中放置