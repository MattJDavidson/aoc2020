#!/usr/bin/env python3
import re
import sys
from typing import Dict, List


Passport = Dict[str, str]


def check_height(height: str) -> bool:
    if not any(unit in height for unit in ["cm", "in"]):
        return False
    return (
        150 <= int(height[:-2]) <= 193
        if "cm" in height
        else 59 <= int(height[:-2]) <= 76
    )


def is_valid(passport: Passport) -> bool:
    return all(field in passport for field in REQUIRED_FIELDS)


def fields_validated(passport: Passport) -> bool:
    return is_valid(passport) and all(
        REQUIRED_FIELDS[field](passport[field]) for field in REQUIRED_FIELDS
    )


def passport_from_lines(lines: List[str]) -> Passport:
    return dict(part.split(":") for part in (lines))


REQUIRED_FIELDS = {
    "byr": lambda k: 1920 <= int(k) <= 2002,
    "iyr": lambda k: 2010 <= int(k) <= 2020,
    "eyr": lambda k: 2020 <= int(k) <= 2030,
    "hgt": check_height,
    "hcl": lambda k: re.match("^#[a-f\d]{6}$", k) != None,
    "ecl": lambda k: k in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda k: len(k) == 9,
}


def main():
    lines = [line for line in open("../inputs/04_01.txt", "r")]
    passport_lines = [
        line.replace("\n", " ").rstrip() for line in "".join(lines).split("\n\n")
    ]
    passports = [
        passport_from_lines(passport_info.split()) for passport_info in passport_lines
    ]
    print(sum(map(is_valid, passports)))
    print(sum(map(fields_validated, passports)))


if __name__ == "__main__":
    sys.exit(main())
