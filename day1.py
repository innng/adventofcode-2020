from itertools import combinations

if __name__ == "__main__":
    # part 1
    with open("input/day1.txt") as fp:
        nums = fp.readlines()
        nums = [int(x.strip()) for x in nums]

    for num1, num2 in combinations(nums, 2):
        if num1 + num2 == 2020:
            print(f"part 1: {num1 * num2}")
            break

    # part 2
    for num1, num2, num3 in combinations(nums, 3):
        if num1 + num2 + num3 == 2020:
            print(f"part 2: {num1 * num2 * num3}")
            break
