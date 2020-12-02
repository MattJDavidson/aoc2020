#!/usr/bin/env python3
import sys


def product_of_first_two_sums_that_equal_twenty_twenty(nums):
    for num in nums:
        if (2020 - num) in nums:
            return num * (2020 - num)


def product_of_first_three_sums_that_equal_twenty_twenty(nums):
    for x in nums:
        for y in nums:
            if (2020 - x - y) in nums:
                return x * y * (2020 - x - y)


def main():
    inputs = [int(line.strip()) for line in open("inputs/01_1.txt", "r")]
    print(product_of_first_two_sums_that_equal_twenty_twenty(inputs))
    print(product_of_first_three_sums_that_equal_twenty_twenty(inputs))


if __name__ == "__main__":
    sys.exit(main())
