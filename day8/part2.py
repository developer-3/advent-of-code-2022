#!/usr/bin/env python3

from collections import defaultdict
import numpy as np

def main():

    graph = []

    with open("input.txt") as f:
        for line in f.readlines():
            graph.append([int(x) for x in line.strip()])

    n = len(graph)
    m = len(graph[0])

    visited = defaultdict(set)

    max_scenic_score = float("-inf")

    stack = [(1,1)]

    while stack:
        (r,c) = stack.pop()

        if (r,c) in visited:
            continue
        
        visited[(r,c)] = 1

        curr = graph[r][c]

        # if you are reading this, this code is not a representation for 
        # my abilities, I just want to solve these problems by any means
        # necessary and if that means very gross looking code that will 
        # immediately become legacy the second I "git push", then yes
        # I will write it but only in this case, please look at other
        # repos of mine and not just these solutions, I write much better
        # looking code I promise.  ok happy reading thank you bye <3 

        curr_score = []

        trees = 0
        for t in graph[r][:c][::-1]:
            trees += 1
            if int(t) >= int(curr):
                break

        curr_score.append(trees)
        
        trees = 0
        for t in graph[r][c+1:n]:
            trees += 1
            if int(t) >= int(curr):
                break

        curr_score.append(trees)
        
        trees = 0
        for t in graph[:r][::-1]:
            trees += 1
            if int(t[c]) >= int(curr):
                break

        curr_score.append(trees)
        
        trees = 0
        for t in graph[r+1:m]:
            trees += 1
            if int(t[c]) >= int(curr):
                break
        
        curr_score.append(trees)

        max_scenic_score = max(np.prod(curr_score), max_scenic_score)

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

    print(max_scenic_score)


if __name__ == "__main__":
    main()