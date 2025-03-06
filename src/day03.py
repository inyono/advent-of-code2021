"""
See: https://adventofcode.com/2021/day/3 (Day 3: Binary Diagnostic)
"""

from typing import TextIO


class Day03:
    def __init__(self, stream: TextIO) -> None:
        self.numbers = [line.strip() for line in stream]

    def solve_part1(self) -> int:
        # Check if self.numbers is empty
        if not self.numbers:
            return 0

        bits = len(self.numbers[0])
        count_ones = [0] * bits
        for number in self.numbers:
            for i, bit in enumerate(number):
                if bit == "1":
                    count_ones[i] += 1

        gamma = int(
            "".join(
                [
                    "1" if count > len(self.numbers) - count else "0"
                    for count in count_ones
                ]
            ),
            2,
        )
        epsilon = ~gamma & ((1 << bits) - 1)
        return gamma * epsilon

    def solve_part2(self) -> int:
        return 0
