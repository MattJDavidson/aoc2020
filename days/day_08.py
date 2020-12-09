#!/usr/bin/env python3
import itertools
import sys
from typing import Tuple, List

Op = str
Command = Tuple[Op, int]


def get_accumulator_for_exit(commands: List[Command]) -> Tuple[int, int]:
    visited = set()
    index = 0
    count = 0
    while index not in visited and index < len(commands):
        visited.add(index)
        op, num = commands[index]
        if "jmp" in op:
            index += num
            continue
        if "acc" in op:
            count += num
        index += 1
    return count, index


def flip_command(command: Command) -> Command:
    return {"jmp": "nop", "nop": "jmp"}[command[0]], command[1]


def get_accumulator_for_exit_after_fix(commands: List[Command]) -> Tuple[int, int]:
    potential_corrupt_indexes = filter(
        lambda c: c[0][0] != "acc", zip(commands, itertools.count())
    )
    for _, i in potential_corrupt_indexes:
        mutated_commands = commands[:]
        mutated_commands[i] = flip_command(mutated_commands[i])

        count, index = get_accumulator_for_exit(mutated_commands)
        if index == len(commands):
            return count, index

    return -1, -1


def main():
    lines = [line.strip() for line in open("../inputs/08_01.txt", "r")]
    commands = []
    for line in lines:
        op, i = line.split()
        commands.append((op, int(i)))

    print(get_accumulator_for_exit(commands)[0])
    print(get_accumulator_for_exit_after_fix(commands)[0])


if __name__ == "__main__":
    sys.exit(main())
