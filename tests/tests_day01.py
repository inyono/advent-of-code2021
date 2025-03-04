import io
import unittest

from src.day01 import Day01


class Day01TestCase(unittest.TestCase):
    def setUp(self):
        example = """199
200
208
210
200
207
240
269
260
263"""
        self.day01 = Day01(io.StringIO(example))

    def test_part1(self):
        self.assertEqual(7, self.day01.solve_part1())

    def test_part2(self):
        self.assertEqual(5, self.day01.solve_part2())


if __name__ == "__main__":
    unittest.main()
