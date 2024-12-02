def parse_report(file_path):
    with open(file_path) as file:
        return [list(map(int, line.strip().split())) for line in file]


def check_validity(seq):
    return (
            all(0 < seq[i + 1] - seq[i] <= 3 for i in range(len(seq) - 1)) or
            all(-3 <= seq[i + 1] - seq[i] < 0 for i in range(len(seq) - 1)))


def part1(sequences):
    return sum(check_validity(seq) for seq in sequences)


def part2(sequences):
    return sum(any(check_validity(seq[:i] + seq[i + 1:]) for i in range(len(seq) + 1)) for seq in sequences)


def main():
    sequences = parse_report("report.txt")
    print("Part 1:", part1(sequences))
    print("Part 2:", part2(sequences))


if __name__ == "__main__":
    main()
