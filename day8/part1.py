#!/usr/bin/env python3

# I did not enjoy this problem at all

from collections import defaultdict

def main():

    graph = []

    with open("input.txt") as f:
        for line in f.readlines():
            graph.append([int(x) for x in line.strip()])

    n = len(graph)
    m = len(graph[0])

    visited = defaultdict(set)

    total = [0]

    stack = [(1,1)]

    while stack:
        (r,c) = stack.pop()

        if (r,c) in visited:
            continue
        
        visited[(r,c)] = 1

        visible = False

        curr = graph[r][c]
        for t in graph[r][:c]:
            if int(t) >= int(curr):
                break
        else:
            total[0] += 1
            visible = True
        
        if visible is False:
            for t in graph[r][c+1:n]:
                if int(t) >= int(curr):
                    break
            else:
                total[0] += 1
                visible = True

        if visible is False:
            for t in graph[:r]:
                if int(t[c]) >= int(curr):
                    break
            else:
                total[0] += 1
                visible = True

        if visible is False:
            for t in graph[r+1:m]:
                if int(t[c]) >= int(curr):
                    break
            else:
                total[0] += 1
                visible = True

        if r > 1:
            # go up
            stack.append((r-1,c))

        if c < m-2:
            # go right
            stack.append((r,c+1))
        
        if r < n-2:
            # go down
            stack.append((r+1,c))

        if c > 1:
            # go left
            stack.append((r,c-1))


    total[0] += (m-2)*4 + 4
    print(total[0])


if __name__ == "__main__":
    main()