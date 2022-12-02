#!/usr/bin/env python3

def main():
    part1()
    part2()

def part1():
    guide = {"A":1, "X": 1, "B":2, "Y": 2, "C":3, "Z": 3}

    outcomes= {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,

        ("B", "X"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,

        ("C", "X"): 6,
        ("C", "Y"): 0,
        ("C", "Z"): 3
    }

    total = 0

    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip().split()

            opponent, me = line[0], line[1]

            total += guide[me]

            total += outcomes[(opponent, me)]

    print(f"Part 1 : Total score after all rounds is {total}")

def part2():
    guide = {"A":1, "X": 1, "B":2, "Y": 2, "C":3, "Z": 3}

    outcomes= {
        ("A", "X"): 3,
        ("A", "Y"): 4,
        ("A", "Z"): 8,

        ("B", "X"): 1,
        ("B", "Y"): 5,
        ("B", "Z"): 9,

        ("C", "X"): 2,
        ("C", "Y"): 6,
        ("C", "Z"): 7
    }

    total = 0

    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip().split()

            opponent, me = line[0], line[1]

            total += outcomes[(opponent, me)]

    print(f"Part 2 : Total score after all rounds is {total}")

if __name__ == "__main__":
    main()
