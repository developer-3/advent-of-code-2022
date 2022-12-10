#!/usr/bin/env python3

def main():

    register_x = 1
    cycle = 0

    boost = [20, 60, 100, 140, 180, 220]

    strengths = []

    with open("input.txt") as f:
        addx = False
        for line in f.readlines():
            instruction = line.strip().split()

            if instruction[0] == "addx":
                addx = True
                cycle += 1

                if cycle in boost:
                    strengths.append(cycle * register_x)

            cycle += 1

            if cycle in boost:
                strengths.append(cycle * register_x)

            if addx:
                register_x += int(instruction[1])
                addx = not addx


    print(sum(strengths))

if __name__ == "__main__":
    main()