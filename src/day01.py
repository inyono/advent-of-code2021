class Day01:
    def __init__(self, stream):
        self.numbers = [int(line.strip()) for line in stream]

    def solve_part1(self):
        result = 0
        previous = self.numbers[0]
        for number in self.numbers[1:]:
            if number > previous:
                result += 1
            previous = number
        return result

    def solve_part2(self):
        result = 0
        previous = sum(self.numbers[:3])
        for i in range(3, len(self.numbers)):
            acc = previous + self.numbers[i] - self.numbers[i - 3]
            if acc > previous:
                result += 1
            previous = acc
        return result
