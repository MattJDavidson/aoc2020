#!/usr/bin/env python3
import sys


def convert_to_binary_string(boarding_string: str) -> str:
    if boarding_string == "":
        return ""
    if boarding_string[0] in "FL":
        return "0" + convert_to_binary_string(boarding_string[1:])
    return "1" + convert_to_binary_string(boarding_string[1:])


def calculate_seat_id(boarding_pass: str) -> int:
    return (int(convert_to_binary_string(boarding_pass[:7]), 2) * 8) + int(
        convert_to_binary_string(boarding_pass[7:]), 2
    )


def main():
    boarding_passes = [line.strip() for line in open("../inputs/05_01.txt", "r")]
    occupied_seats = set(map(calculate_seat_id, boarding_passes))

    print(max(occupied_seats))
    print(
        next(
            filter(
                lambda i: i - 1 in occupied_seats
                and i + 1 in occupied_seats
                and i not in occupied_seats,
                range(
                    0 + 8 + 1, 1024 - 8 - 1
                ),  # don't check first or last rows, or their first and last seats
            )
        )
    )


if __name__ == "__main__":
    sys.exit(main())
