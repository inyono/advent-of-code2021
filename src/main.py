from pathlib import Path

from src.day01 import Day01
from src.day02 import Day02
from src.day03 import Day03

if __name__ == "__main__":
    print("--- Day 1: Sonar Sweep ---")
    with open(Path(__file__).parent.parent / "inputs" / "day01.txt", "r") as f:
        day01 = Day01(f)
        print(f"Part 1: {day01.solve_part1()}")
        print(f"Part 2: {day01.solve_part2()}")

    print("--- Day 2: Dive! ---")
    with open(Path(__file__).parent.parent / "inputs" / "day02.txt", "r") as f:
        day02 = Day02(f)
        print(f"Part 1: {day02.solve_part1()}")
        print(f"Part 2: {day02.solve_part2()}")

    print("--- Day 3: Binary Diagnostic ---")
    with open(Path(__file__).parent.parent / "inputs" / "day03.txt", "r") as f:
        day03 = Day03(f)
        print(f"Part 1: {day03.solve_part1()}")
        print(f"Part 2: {day03.solve_part2()}")
