import unittest
from maze import Maze
from graphics import Window, Point, Line

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(cell.visited, False)

    def test_create_point(self):
        point = Point(100, 150)
        self.assertEqual(point._x, 100)
        self.assertEqual(point._y, 150)

    def test_create_line(self):
        p1 = Point(50, 50)
        p2 = Point(200, 100)
        line = Line(p1, p2)
        self.assertEqual(line._p1._x, 50)
        self.assertEqual(line._p1._y, 50)
        self.assertEqual(line._p2._x, 200)
        self.assertEqual(line._p2._y, 100)

if __name__ == "__main__":
    import sys
    flags = sys.argv[1:]  # Get command-line arguments excluding the script name
    if "-m" in flags:
        # Run only maze-related tests
        suite = unittest.TestSuite()
        suite.addTest(Tests("test_maze_create_cells"))
        suite.addTest(Tests("test_maze_create_cells_large"))
        suite.addTest(Tests("test_maze_reset_cells_visited"))
        unittest.TextTestRunner().run(suite)
    elif "-g" in flags:
        # Run only graphics-related tests
        suite = unittest.TestSuite()
        suite.addTest(Tests("test_create_point"))
        suite.addTest(Tests("test_create_line"))
        unittest.TextTestRunner().run(suite)
    else:
        # Run all tests
        unittest.main()
