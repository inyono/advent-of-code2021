import io
import unittest

from src.day03 import Day03


class Day03TestCase(unittest.TestCase):
    def setUp(self):
        example = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
        self.day03 = Day03(io.StringIO(example))

    def test_part1(self):
        self.assertEqual(198, self.day03.solve_part1())

    def test_part2(self):
        self.assertEqual(230, self.day03.solve_part2())


if __name__ == "__main__":
    unittest.main()
