if __name__ == "__main__":
    # part 1
    with open("input/day3.txt") as fp:
        lines = fp.readlines()

    lines = [x.strip() for x in lines]

    pos = 0
    skip = 3
    trees = 0

    for line in lines:
        if line[pos % len(line)] == "#":
            trees += 1

        pos += skip

    print(f"part 1: {trees}")

    # part 2
    with open("input/day3.txt") as fp:
        lines = fp.readlines()

    lines = [x.strip() for x in lines]

    skips = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1

    for right, down in skips:
        trees = 0
        pos = 0
        skip_next_line = 0

        for line in lines:
            skip_next_line += 1

            if down == 2 and skip_next_line % 2 == 0:
                continue

            if line[pos % len(line)] == "#":
                trees += 1

            pos += right

        total *= trees

    print(f"part 2: {total}")
