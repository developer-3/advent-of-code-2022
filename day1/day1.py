#!/usr/bin/env python3

def main():
    elves = [0]
    with open("input.txt") as f:
        for line in f.readlines():
            if line.strip() != "":
                elves[len(elves)-1] += int(line)
            else:
                elves.append(0)

    print(f"{max(elves)} is the most amount of calories")

    elves.sort(reverse=True)

    print(f"The top 3 elves are carrying {elves[0:3]} or {sum(elves[0:3])} total calories")


if __name__ == "__main__":
    main()
