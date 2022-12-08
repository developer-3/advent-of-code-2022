#!/usr/bin/env python3

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
    
    MAX_STORAGE = 100_000

    result = []
    while curr_node != head:
        if len(curr_node.children) != 0:
            for node in nodes:
                if node.name in curr_node.children and node.parent.name == curr_node.name:
                    curr_node = node
                    nodes.remove(node)
                    break
            continue

        if curr_node.size <= MAX_STORAGE:
            result.append(curr_node.size)

        parent = curr_node.parent
        try:
            parent.children.remove(curr_node.name)
            parent.size += curr_node.size
        except:
            pass

        curr_node = parent

    print(sum(result))


    


if __name__ == "__main__":
    main()