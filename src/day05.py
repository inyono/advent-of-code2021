"""
See: https://adventofcode.com/2021/day/5 (Day 5: Hydrothermal Venture)
"""

from typing import TextIO


type Point = tuple[int, int]


class Line:
    def __init__(self, line: str) -> None:
        start, end = line.split(" -> ")
        self.point1: Point = Line.parse_point(start)
        self.point2: Point = Line.parse_point(end)

    def covered_points(self) -> list[Point]:
        if self.is_horizontal:
            start = min(self.point1[0], self.point2[0])
            end = max(self.point1[0], self.point2[0])
            return [(start + i, self.point1[1]) for i in range(end - start + 1)]
        elif self.is_vertical:
            start = min(self.point1[1], self.point2[1])
            end = max(self.point1[1], self.point2[1])
            return [(self.point1[0], start + i) for i in range(end - start + 1)]
        else:
            return []

    @property
    def is_horizontal(self) -> bool:
        return self.point1[1] == self.point2[1]

    @property
    def is_vertical(self) -> bool:
        return self.point1[0] == self.point2[0]

    @staticmethod
    def parse_point(input: str) -> Point:
        x, y = input.split(",")
        return int(x), int(y)


class Day05:
    def __init__(self, input_file: TextIO) -> None:
        self.lines = [Line(line.strip()) for line in input_file]
        return

    def solve_part1(self) -> int:
        relevant_lines = [
            line for line in self.lines if line.is_horizontal or line.is_vertical
        ]
        result = 0
        points: dict[Point, int] = {}
        for line in relevant_lines:
            for point in line.covered_points():
                if point in points:
                    points[point] += 1
                    if points[point] == 2:
                        result += 1
                else:
                    points[point] = 1
        return result

    def solve_part2(self) -> int:
        return 0
