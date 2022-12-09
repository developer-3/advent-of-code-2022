#!/usr/bin/env python3

from collections import defaultdict

def main():

    knots = [(0,0) for _ in range(10)]

    visited = defaultdict(set)

    head, tail = 0, 9

    visited[knots[tail]] = 1

    with open("input.txt") as f:
        for line in f.readlines():
            instruction = line.strip().split()

            for _ in range(int(instruction[1])):
                if instruction[0] == "R":
                    knots[head] = (knots[head][0]+1, knots[head][1])
                elif instruction[0] == "L":
                    knots[head] = (knots[head][0]-1, knots[head][1])
                elif instruction[0] == "U":
                    knots[head] = (knots[head][0], knots[head][1]+1)
                elif instruction[0] == "D":
                    knots[head] = (knots[head][0], knots[head][1]-1)
                
                # check adjacency and move knots
                for k in range(1, len(knots)):
                    x_diff, y_diff = knots[k][0] - knots[k-1][0], knots[k][1] - knots[k-1][1]

                    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
                        break

                    if abs(x_diff) > 1:
                        if abs(x_diff) == x_diff:
                            x_diff -= 1
                        else:
                            x_diff += 1

                    if abs(y_diff) > 1:
                        if abs(y_diff) == y_diff:
                            y_diff -= 1
                        else:
                            y_diff += 1

                    knots[k] = (knots[k][0]-x_diff, knots[k][1]-y_diff)
                    

                visited[knots[tail]] = 1

    print(len(visited.keys()))
            

if __name__ == "__main__":
    main()