from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze1 = Maze(30,20, 5,8,70,50,win)
    win.wait_for_close()


main()