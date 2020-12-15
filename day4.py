import re


def validate_fields(line):
    line = line.split()

    for field in line:
        if "byr" in field:
            _, value = field.split(":")
            if not (2002 >= int(value) >= 1920):
                return False

        if "iyr" in field:
            _, value = field.split(":")
            if not (2020 >= int(value) >= 2010):
                return False

        if "eyr" in field:
            _, value = field.split(":")
            if not (2030 >= int(value) >= 2020):
                return False

        if "hgt" in field:
            _, value = field.split(":")
            num = re.findall(r"[A-Za-z]+|\d+", value)[0]

            if "cm" in value:
                if not (193 >= int(num) >= 150):
                    return False
            elif "in" in value:
                if not (76 >= int(num) >= 59):
                    return False
            else:
                return False

        if "hcl" in field:
            _, value = field.split(":")
            if "#" not in value or len(value) != 7:
                return False

            pattern = re.compile("#[0-9a-f]{6}")
            if not pattern.match(value):
                return False

        if "ecl" in field:
            _, value = field.split(":")
            if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False

        if "pid" in field:
            _, value = field.split(":")
            if len(value) != 9 or re.search("[a-zA-Z]", value):
                return False

    return True


if __name__ == "__main__":
    # part 1
    with open("input/day4.txt") as fp:
        lines = fp.read()

    lines = lines.split("\n\n")
    lines = [x.replace("\n", " ") for x in lines]

    fields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    valid = 0

    for line in lines:
        if all(x in line for x in fields):
            valid += 1

    print(f"part 1: {valid}")

    # part 2
    with open("input/day4.txt") as fp:
        lines = fp.read()

    lines = lines.split("\n\n")
    lines = [x.replace("\n", " ") for x in lines]

    fields = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    valid = 0

    for line in lines:
        if all(x in line for x in fields):
            if validate_fields(line):
                valid += 1

    print(f"part 2: {valid}")
