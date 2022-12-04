#!/usr/bin/env python3

def main():

    res = 0

    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip().split(",")

            elf1, elf2 = line[0].split("-"), line[1].split("-")

            # check if elf1 contains elf2
            if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
                res += 1
            # check if elf2 contains elf1
            elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
                res += 1

    print(f"There are {res} number of assignment pairs that fully contain each other")

if __name__ == "__main__":
    main()
