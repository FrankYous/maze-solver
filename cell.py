from graphics import Point, Line


class Cell:
    def __init__(self, x1, y1, x2, y2, win = None):
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
        if self._win is None:
            return

        linel = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(linel, "black")
        else:
            self._win.draw_line(linel, "white")
        
        liner = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.has_right_wall:
            self._win.draw_line(liner, "black")
        else:
            self._win.draw_line(liner, "white")
        
        linet = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.has_top_wall:
            self._win.draw_line(linet, "black")
        else:
            self._win.draw_line(linet, "white")
        
        lineb = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(lineb, "black")
        else:
            self._win.draw_line(lineb, "white")

    def draw_move(self, to_cell, undo=False):
        if not undo:
            color = "red"
        else:
            color = "gray"
        line = Line(
            Point((self._x1 + self._x2)/2,(self._y1+self._y2)/2), 
            Point((to_cell._x1 + to_cell._x2)/2,(to_cell._y1+to_cell._y2)/2))
        self._win.draw_line(line, color)
        