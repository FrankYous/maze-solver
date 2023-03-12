from tkinter import Tk, BOTH, Canvas

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
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

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
        if self.has_left_wall == True:
            linel = Line(self._x1, self._y1, self._x1, self._y2)
            self._win.draw_line(linel,"red")
        if self.has_right_wall == True:
            liner = Line(self._x2, self._y1, self._x2, self._y2)
            self._win.draw_line(liner,"blue")
        if self.has_top_wall == True:
            linet = Line(self._x1, self._y1, self._x2, self._y1)
            self._win.draw_line(linet, "green")
        if self.has_bottom_wall == True:
            lineb = Line(self._x1, self._y2, self._x2, self._y2)
            self._win.draw_line(lineb, "black")

def main():
    win = Window(800, 600)
    cell1 = Cell(100,100,400,400,win)
    cell1.has_left_right = True
    cell1.draw()
    win.wait_for_close()


main()