"""
See: https://adventofcode.com/2021/day/2 (Day 2: Dive!)
"""

from enum import Enum
from typing import TextIO


class Command(Enum):
    FORWARD = "forward"
    UP = "up"
    DOWN = "down"


class Day02:
    def __init__(self, stream: TextIO) -> None:
        self.instructions = [
            (Command(cmd), int(val))
            for cmd, val in [line.strip().split() for line in stream]
        ]

    def solve_part1(self) -> int:
        x, y = 0, 0
        for cmd, val in self.instructions:
            match cmd:
                case Command.FORWARD:
                    x += val
                case Command.UP:
                    y -= val
                case Command.DOWN:
                    y += val
        return x * y

    def solve_part2(self) -> int:
        x, y, aim = 0, 0, 0
        for cmd, val in self.instructions:
            match cmd:
                case Command.FORWARD:
                    x += val
                    y += aim * val
                case Command.UP:
                    aim -= val
                case Command.DOWN:
                    aim += val
        return x * y
