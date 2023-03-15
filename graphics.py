from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(height = height, width = width)
        self.canvas.pack()
        self.running = False        

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.running = False


class Point:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord


class Line:
    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.x2 = point2.x
        self.y1 = point1.y
        self.y2 = point2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2
        )
        canvas.pack()


class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            linel = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(linel, "black")
        if self.has_right_wall:
            liner = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(liner, "black")
        if self.has_top_wall:
            linet = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(linet, "black")
        if self.has_bottom_wall:
            lineb = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(lineb, "black")

    def draw_move(self, to_cell, undo=False):
        if undo == False:
            color = "red"
        else:
            color = "gray"
        line = Line(
            Point((self._x1 + self._x2)/2,(self._y1+self._y2)/2), 
            Point((to_cell._x1 + to_cell._x2)/2,(to_cell._y1+to_cell._y2)/2))
        self._win.draw_line(line, color)


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