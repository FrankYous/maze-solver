from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze1 = Maze(50,50, 25,30,20,20,win,245)
    maze1.solve()
    win.wait_for_close()


main()