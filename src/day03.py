"""
See: https://adventofcode.com/2021/day/3 (Day 3: Binary Diagnostic)
"""

from typing import TextIO, Callable, Union, Literal

type Bit = Union[Literal["0"], Literal["1"]]


class Day03:
    def __init__(self, stream: TextIO) -> None:
        self.numbers = [line.strip() for line in stream]

    def solve_part1(self) -> int:
        return self.gamma * self.epsilon

    def solve_part2(self) -> int:
        return self.oxygen_generator_rating * self.co2_scrubber_rating

    @property
    def gamma(self) -> int:
        if not self.numbers:
            return 0
        bits = self.bits
        count_ones = [self.most_common_bit(self.numbers, i) for i in range(bits)]
        return int("".join(count_ones), 2)

    @property
    def epsilon(self) -> int:
        if not self.numbers:
            return 0
        return ~self.gamma & ((1 << self.bits) - 1)

    @property
    def oxygen_generator_rating(self) -> int:
        return self.filter_by_bit_criteria(self.most_common_bit)

    @property
    def co2_scrubber_rating(self) -> int:
        return self.filter_by_bit_criteria(self.least_common_bit)

    def filter_by_bit_criteria(
        self, criteria_fn: Callable[[list[str], int], Bit]
    ) -> int:
        if not self.numbers:
            return 0
        remaining = self.numbers
        index = 0
        while index < self.bits and len(remaining) > 1:
            criteria_bit = criteria_fn(remaining, index)
            remaining = [
                number for number in remaining if number[index] == criteria_bit
            ]
            index += 1
        return int(remaining[0], 2)

    @property
    def bits(self) -> int:
        if not self.numbers:
            return 0
        return len(self.numbers[0])

    @staticmethod
    def most_common_bit(numbers: list[str], index: int) -> Bit:
        ones = sum(1 for number in numbers if number[index] == "1")
        return "1" if ones >= len(numbers) / 2 else "0"

    @staticmethod
    def least_common_bit(numbers: list[str], index: int) -> Bit:
        return "0" if Day03.most_common_bit(numbers, index) == "1" else "1"
