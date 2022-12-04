#!/usr/bin/env python3

def main():

    res = 0

    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip().split(",")

            elf1, elf2 = [int(x) for x in line[0].split("-")], [int(x) for x in line[1].split("-")]

            elf1 = set(range(elf1[0], elf1[1]+1))
            elf2 = set(range(elf2[0], elf2[1]+1))

            if len(elf1.intersection(elf2)):
                res += 1
                print(line)


    print(f"There are {res} number of assignment pairs that overlap")

if __name__ == "__main__":
    main()
