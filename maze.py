from graphics import Window
from cell import Cell
import time


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(0,self.num_cols):
            row = []
            for j in range(0,self.num_rows):
                row.append(Cell(self.x1,self.y1,self.x1+self.cell_size_x,self.y1+self.cell_size_y,self._win))
            self._cells.append(row)
        for i in range(0,self.num_cols):
            for j in range(0,self.num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self,i,j):
        self.xs = self.x1 + i * self.cell_size_x
        self.xe = self.xs + self.cell_size_x
        self.ys = self.y1 + j * self.cell_size_y
        self.ye = self.ys + self.cell_size_y
        cell1 = Cell(self.xs,self.ys,self.xe, self.ye,self._win)
        cell1.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep (0.05)


def main():
    win = Window(800, 600)
    maze1 = Maze(30,20, 5,8,70,50,win)
    win.wait_for_close()


main()