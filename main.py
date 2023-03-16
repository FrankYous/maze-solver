from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze1 = Maze(20,20, 20,30,20,20,win)
    win.wait_for_close()


main()