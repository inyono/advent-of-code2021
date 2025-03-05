import io
import unittest

from src.day02 import Day02


class Day02TestCase(unittest.TestCase):
    def setUp(self):
        example = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
        self.day02 = Day02(io.StringIO(example))

    def test_part1(self):
        self.assertEqual(150, self.day02.solve_part1())


if __name__ == "__main__":
    unittest.main()
