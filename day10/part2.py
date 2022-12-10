#!/usr/bin/env python3

def main():

    register_x = 1
    cycle = -1

    sprite_position = 1

    drawing = []

    with open("input.txt") as f:
        addx = False
        for line in f.readlines():
            instruction = line.strip().split()

            if instruction[0] == "addx":
                addx = True
                cycle += 1

                if cycle >= 40:
                    cycle = 0

                # draw pixel
                if cycle in [sprite_position-1, sprite_position, sprite_position+1]:
                    drawing.append("#")
                else:
                    drawing.append(".")

            cycle += 1
            if cycle >= 40:
                cycle = 0

            # draw pixel
            if cycle in [sprite_position-1, sprite_position, sprite_position+1]:
                    drawing.append("#")
            else:
                drawing.append(".")
            

            if addx:
                register_x += int(instruction[1])
                addx = not addx

            sprite_position = register_x


    for i in range(0, 7):
        print(''.join(drawing[i*40:i*40+40]))

if __name__ == "__main__":
    main()