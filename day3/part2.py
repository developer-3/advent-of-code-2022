#!/usr/bin/env python3

def main():

    res = 0

    with open("input.txt") as f:

        lines = f.readlines()

        for i in range(0, len(lines), 3):
            one, two, three = [set(lines[i].strip()), set(lines[i+1].strip()), set(lines[i+2].strip())]

            shared = one.intersection(two.intersection(three)).pop()
            print(shared)
            if shared.islower():
                res += ord(shared.upper()) - 64
            else:
                res += ord(shared.lower()) - 70

    print(f"The total sum of the priority items is {res}.")


if __name__ == "__main__":
    main()
