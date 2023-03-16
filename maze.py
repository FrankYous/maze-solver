from cell import Cell
import time
import random


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None,    
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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

    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        to_visit = []
        if i > 0:
            to_visit.append([i-1,j])
        if i < self.num_cols-1:
            to_visit.append([i+1,j])
        if j > 0:
            to_visit.append([i,j-1])
        if j < self.num_rows-1:
            to_visit.append([i,j+1])

        while to_visit != []:
            dir = random.randrange(len(to_visit))
            coord = to_visit.pop(dir)
            cx = coord [0]
            cy = coord [1]
        
            if cx == i+1 and self._cells[i+1][j].visited == False:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._break_walls_r(i+1,j)

            if cy == j+1 and self._cells[i][j+1].visited == False:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._break_walls_r(i,j+1)                  

            if cx == i-1 and self._cells[i-1][j].visited == False:
                self._cells[i-1][j].has_right_wall = False
                self._cells[i][j].has_left_wall = False
                self._break_walls_r(i-1,j)

            if cy == j-1 and self._cells[i][j-1].visited == False:
                self._cells[i][j-1].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
                self._break_walls_r(i,j-1)
                 
            self._draw_cell(i,j)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _draw_cell(self,i,j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        #time.sleep (0.05)

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True

        # Moving right
        if (i < self.num_cols-1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i+1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j],True)

        # Moving down
        if (j < self.num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j+1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1],True)

        # Moving left
        if (i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j],True)

        # Moving up
        if (j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j-1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1],True)
        
        return False