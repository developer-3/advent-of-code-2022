#!/usr/bin/env python3

import re

def main():
    with open("input.txt") as f:

        data = []

        while True:
            line = f.readline()
            if line == "\n":
                break
            data.append(line)

        n = data[len(data)-1].strip()
        crates = {x: [] for x in range(int(n[len(n)-1]))}

        # [ 1 ] _ [ 5 ] _

        # 0 : 1
        # 1 : 5
        # 2 : 9
        # 3 : 13 

        for width in data[:len(data)-1]:
            j = -1
            for i in range(1, len(width), 4):
                j += 1
                if width[i] == " ":
                    continue
                curr = crates[i - 3*j - 1]
                curr.append(width[i])
                crates[i - 3*j - 1] = curr

        for line in f.readlines():
            line = re.sub(r"\D", "", line)
            
            if len(line) == 4:
                move, fro, to = int(line[:2]), int(line[2:3])-1, int(line[3:])-1
            else:
                move, fro, to = int(line[:1]), int(line[1:2])-1, int(line[2:])-1

            rearrang = crates[fro]
            rearrang = rearrang[:move]
            
            for i in range(move):
                crates[fro].pop(0)

            curr = crates[to]
            rearrang.reverse()
            crates[to] = rearrang + curr

        top = [x[0] for x in crates.values()]
        print(f"The crates on top after movement are {''.join(top)}")


if __name__ == "__main__":
    main()