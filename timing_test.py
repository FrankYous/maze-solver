import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        maze1 = Maze(50,50, 25,30,20,20)
        maze1.solve()
     
if __name__ == "__main__":
    unittest.main()