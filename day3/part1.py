#!/usr/bin/env python3

def main():

    res = 0

    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            n = len(line)
            compartment_one = line[:n//2]
            compartment_two = line[n//2:]

            shared = ""
            for i in compartment_one:
                if i in compartment_two:
                    shared = i
                    break

            if shared.islower():
                res += ord(shared.upper()) - 64
            else:
                res += ord(shared.lower()) - 70

    print(f"The total sum of the priority items is {res}.")


if __name__ == "__main__":
    main()
