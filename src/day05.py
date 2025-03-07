"""
See: https://adventofcode.com/2021/day/5 (Day 5: Hydrothermal Venture)
"""

from typing import TextIO

type Point = tuple[int, int]


class Line:
    def __init__(self, line: str) -> None:
        start, end = line.split(" -> ")
        self.point1: Point = self.parse_point(start)
        self.point2: Point = self.parse_point(end)

    def covered_points(self) -> list[Point]:
        if self.is_horizontal:
            start = min(self.point1[0], self.point2[0])
            end = max(self.point1[0], self.point2[0])
            return [(start + i, self.point1[1]) for i in range(end - start + 1)]
        elif self.is_vertical:
            start = min(self.point1[1], self.point2[1])
            end = max(self.point1[1], self.point2[1])
            return [(self.point1[0], start + i) for i in range(end - start + 1)]
        elif self.is_diagonal:
            top, bottom = (
                (self.point1, self.point2)
                if self.point1[0] < self.point2[0]
                else (self.point2, self.point1)
            )
            step_y = 1 if bottom[1] >= top[1] else -1
            return [
                (x, y)
                for x, y in zip(
                    range(top[0], bottom[0] + 1),
                    range(top[1], bottom[1] + step_y, step_y),
                )
            ]
        else:
            return []

    @property
    def is_horizontal(self) -> bool:
        return self.point1[1] == self.point2[1]

    @property
    def is_vertical(self) -> bool:
        return self.point1[0] == self.point2[0]

    @property
    def is_diagonal(self) -> bool:
        return self.max_x - self.min_x == self.max_y - self.min_y

    @property
    def min_x(self) -> int:
        return min(self.point1[0], self.point2[0])

    @property
    def max_x(self) -> int:
        return max(self.point1[0], self.point2[0])

    @property
    def min_y(self) -> int:
        return min(self.point1[1], self.point2[1])

    @property
    def max_y(self) -> int:
        return max(self.point1[1], self.point2[1])

    @staticmethod
    def parse_point(point: str) -> Point:
        x, y = point.split(",")
        return int(x), int(y)


class Day05:
    def __init__(self, input_file: TextIO) -> None:
        self.lines = [Line(line.strip()) for line in input_file]

    def solve_part1(self) -> int:
        relevant_lines = [
            line for line in self.lines if line.is_horizontal or line.is_vertical
        ]
        return self.count_overlaps(relevant_lines)

    def solve_part2(self) -> int:
        return self.count_overlaps(self.lines)

    @staticmethod
    def count_overlaps(lines: list[Line]) -> int:
        result = 0
        points: dict[Point, int] = {}
        for line in lines:
            for point in line.covered_points():
                if point in points:
                    points[point] += 1
                    if points[point] == 2:
                        result += 1
                else:
                    points[point] = 1
        return result
