"""
See: https://adventofcode.com/2021/day/3 (Day 3: Binary Diagnostic)
"""

from typing import TextIO


class Day03:
    def __init__(self, stream: TextIO) -> None:
        self.numbers = [line.strip() for line in stream]

    def solve_part1(self) -> int:
        if not self.numbers:
            return 0
        return self.gamma() * self.epsilon()

    def solve_part2(self) -> int:
        return self.oxygen_generator_rating() * self.co2_scrubber_rating()

    def gamma(self):
        bits = self.bits()
        count_ones = [self.most_common_bit(self.numbers, i) for i in range(bits)]
        return int("".join(count_ones), 2)

    def epsilon(self):
        return ~self.gamma() & ((1 << len(self.numbers[0])) - 1)

    def oxygen_generator_rating(self):
        remaining = self.numbers
        index = 0
        while index < self.bits() and len(remaining) > 1:
            most_common = self.most_common_bit(remaining, index)
            remaining = [number for number in remaining if number[index] == most_common]
            index += 1
        return int(remaining[0], 2)

    def co2_scrubber_rating(self):
        remaining = self.numbers
        index = 0
        while index < self.bits() and len(remaining) > 1:
            most_common = self.least_common_bit(remaining, index)
            remaining = [number for number in remaining if number[index] == most_common]
            index += 1
        return int(remaining[0], 2)

    def bits(self):
        return len(self.numbers[0])

    @staticmethod
    def most_common_bit(numbers, index):
        count_ones = 0
        for number in numbers:
            if number[index] == "1":
                count_ones += 1
        return "1" if count_ones >= len(numbers) / 2 else "0"

    @staticmethod
    def least_common_bit(numbers, index):
        return "0" if Day03.most_common_bit(numbers, index) == "1" else "1"
