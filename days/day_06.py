#!/usr/bin/env python3
import sys


def main():
    lines = [line for line in open("../inputs/06_01.txt", "r")]
    group_answers = [
        line.replace("\n", " ").rstrip() for line in "".join(lines).split("\n\n")
    ]
    words = [_.split() for _ in group_answers]
    print(sum(map(lambda k: len(set("".join(k))), words)))
    print(sum(map(lambda k: len(set.intersection(*[set(_) for _ in k])), words)))


if __name__ == "__main__":
    sys.exit(main())
