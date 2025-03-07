import io
import unittest

from src.day05 import Day05, Line


class Day05TestCase(unittest.TestCase):
    def setUp(self):
        example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
        self.day05 = Day05(io.StringIO(example))

    def test_part1(self):
        self.assertEqual(5, self.day05.solve_part1())

    def test_part2(self):
        self.assertEqual(12, self.day05.solve_part2())

    def test_horizontal_line(self):
        line = Line("1,1 -> 1,3")
        self.assertEqual(line.covered_points(), [(1, 1), (1, 2), (1, 3)])

    def test_vertical_line(self):
        line = Line("9,7 -> 7,7")
        self.assertEqual(line.covered_points(), [(7, 7), (8, 7), (9, 7)])

    def test_diagonal_line_bottom_right(self):
        line = Line("1,1 -> 3,3")
        self.assertEqual(line.covered_points(), [(1, 1), (2, 2), (3, 3)])

    def test_diagonal_line_top_right(self):
        line = Line("9,7 -> 7,9")
        self.assertEqual(line.covered_points(), [(7, 9), (8, 8), (9, 7)])


if __name__ == "__main__":
    unittest.main()
