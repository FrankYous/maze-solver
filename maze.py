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
            win = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = []

        for i in range(0,self.num_cols):
            row = []
            for j in range(0,self.num_rows):
                xs = self.x1 + i * self.cell_size_x
                xe = xs + self.cell_size_x
                ys = self.y1 + j * self.cell_size_y
                ye = ys + self.cell_size_y
                row.append(Cell(xs,ys,xe,ye,self._win))
            self._cells.append(row)

        for i in range(0,self.num_cols):
            for j in range(0,self.num_rows):
                self._draw_cell(i,j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _draw_cell(self,i,j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep (0.05)