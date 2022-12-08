#!/usr/bin/env python3

TOTAL_STORAGE = 70_000_000
UPDATE_STORAGE = 30_000_000
USED_STORAGE = 40_268_565

class Node:
    def __init__(self, name, parent, children, size=0):
        self.name = name
        self.parent = parent
        self.children = children
        self.size = size

    def __repr__(self):
        return f"Dir: {self.name}, Parent: {self.parent.name}, Size: {self.size}"

def main():

    head = curr_node = Node(None, None, [])

    nodes = []

    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith("$"):
                # handle command
                if "$ cd" in line:
                    if line.endswith(".."):
                        curr_node = curr_node.parent
                    else:
                        new = Node(line[5:], parent=curr_node, children=[])
                        nodes.append(new)
                        curr_node = new
                elif "ls" in line:
                    pass
            else:
                # update files based on ls
                if line.startswith("dir"):
                    curr_node.children.append(line[4:])
                else:
                    curr_node.size += int(line.split(" ")[0])

    free = TOTAL_STORAGE - USED_STORAGE
    need = UPDATE_STORAGE - free

    print(f"I have {TOTAL_STORAGE:,} total")
    print(f"I need {UPDATE_STORAGE:,} space free to update")
    print(f"I currently have used {USED_STORAGE:,} of storage space")
    print(f"Which means I have {free:,} storage free")
    print(f"So I need to free this much storage {need:,}")

    minim = float("inf")

    while curr_node != head:
        if len(curr_node.children) != 0:
            for node in nodes:
                if node.name in curr_node.children and node.parent.name == curr_node.name:
                    curr_node = node
                    nodes.remove(node)
                    break
            continue

        parent = curr_node.parent
        try:
            parent.children.remove(curr_node.name)
            parent.size += curr_node.size
        except:
            pass
        
        if curr_node.size >= need and curr_node.size <= minim:
            minim = curr_node.size

        curr_node = parent

    print(minim)


if __name__ == "__main__":
    main()