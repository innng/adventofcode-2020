if __name__ == "__main__":
    # part 1
    with open("input/day2.txt") as fp:
        lines = fp.readlines()

    lines = [x.strip() for x in lines]
    valid = 0

    for line in lines:
        items = line.split(" ")
        mi, ma = items[0].split("-")
        letter = items[1].strip(":")
        passwd = items[2]

        if int(ma) >= passwd.count(letter) >= int(mi):
            valid += 1

    print(f"part 1: {valid}")

    # part 2
    with open("input/day2.txt") as fp:
        lines = fp.readlines()

    lines = [x.strip() for x in lines]
    valid = 0

    for line in lines:
        items = line.split(" ")
        i1, i2 = items[0].split("-")
        letter = items[1].strip(":")
        passwd = items[2]

        i1 = int(i1) - 1
        i2 = int(i2) - 1

        if (passwd[i1] == letter and passwd[i2] != letter) or (
            passwd[i1] != letter and passwd[i2] == letter
        ):
            valid += 1

    print(f"part 1: {valid}")
