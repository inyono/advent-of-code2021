from pathlib import Path

from src.day01 import Day01
from src.day02 import Day02
from src.day03 import Day03
from src.day04 import Day04
from src.day05 import Day05

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

    print("--- Day 4: Giant Squid ---")
    with open(Path(__file__).parent.parent / "inputs" / "day04.txt", "r") as f:
        day04 = Day04(f)
        print(f"Part 1: {day04.solve_part1()}")
        print(f"Part 2: {day04.solve_part2()}")

    print("--- Day 5: Hydrothermal Venture ---")
    with open(Path(__file__).parent.parent / "inputs" / "day05.txt", "r") as f:
        day05 = Day05(f)
        print(f"Part 1: {day05.solve_part1()}")
        print(f"Part 2: {day05.solve_part2()}")
