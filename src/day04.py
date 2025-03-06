"""
See: https://adventofcode.com/2021/day/4 (Day 3: Day 4: Giant Squid)
"""

from typing import TextIO


class Bingo:
    def __init__(self, board: list[list[int]]) -> None:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.number_to_index = {
            number: (i, j)
            for i, row in enumerate(board)
            for j, number in enumerate(row)
        }
        self.score = sum(number for row in board for number in row)
        self.marked_numbers_per_row = [0] * self.rows
        self.marked_numbers_per_column = [0] * self.cols

    def mark(self, number: int) -> bool:
        index = self.number_to_index.get(number)
        if index is None:
            return False
        i, j = index
        self.marked_numbers_per_row[i] += 1
        self.marked_numbers_per_column[j] += 1
        self.score -= number
        return (
            self.marked_numbers_per_row[i] == self.cols
            or self.marked_numbers_per_column[j] == self.rows
        )


class Day04:
    def __init__(self, stream: TextIO) -> None:
        lines = [line.strip() for line in stream]
        self.numbers = list(map(int, lines[0].split(",")))
        self.boards = []
        board: list[list[int]] = []
        for line in lines[2:]:
            if not line:
                if board:
                    self.boards.append(Bingo(board))
                    board = []
                continue
            board.append(list(map(int, line.split())))
        if board:
            self.boards.append(Bingo(board))

    def solve_part1(self) -> int:
        for number in self.numbers:
            for board in self.boards:
                if board.mark(number):
                    return board.score * number
        return 0

    def solve_part2(self) -> int:
        return 0
