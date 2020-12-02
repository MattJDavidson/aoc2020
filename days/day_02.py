#!/usr/bin/env python3
import sys
from typing import Tuple


def is_password_valid(constraint: Tuple[int, ...], char: str, password: str):
    (minimum, maximum) = constraint
    return minimum <= password.count(char) <= maximum


def is_password_valid_2(constraint: Tuple[int, ...], char: str, password: str):
    (pos1, pos2) = constraint
    return (password[pos1 - 1] == char) ^ (password[pos2 - 1] == char)


def main():
    inputs = [line.split() for line in open("../inputs/02_1.txt", "r")]
    processed_inputs = [
        (tuple(map(int, line[0].split("-"))), line[1][0], line[2]) for line in inputs
    ]
    print(sum([is_password_valid(*args) for args in processed_inputs]))
    print(sum([is_password_valid_2(*args) for args in processed_inputs]))


if __name__ == "__main__":
    sys.exit(main())
