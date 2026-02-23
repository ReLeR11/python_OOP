def print_rhombus(size, stars):
    print(" " * (size - stars) + "* " * stars)


def up_part_rhombus(size):
    for row in range(1, size):
        print_rhombus(size, row)


def down_part_rhombus(size):
    for row in range(size, 0, -1):
        print_rhombus(size, row)


def rhombus(size):
    up_part_rhombus(size)
    down_part_rhombus(size)


size_rhombus = int(input())

rhombus(size_rhombus)
