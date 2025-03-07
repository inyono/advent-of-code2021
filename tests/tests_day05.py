import io
import unittest

from src.day05 import Day05


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
        self.assertEqual(0, self.day05.solve_part2())


if __name__ == "__main__":
    unittest.main()
