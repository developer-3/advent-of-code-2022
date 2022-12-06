#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        buffer = f.readline()

        l, r = 0, 14

        while r <= len(buffer)-1:
            if len(set(buffer[l:r])) == 14:
                break
            
            l += 1
            r += 1

        print(f"There are {r} characters before the start-of-packet marker.")




if __name__ == "__main__":
    main()