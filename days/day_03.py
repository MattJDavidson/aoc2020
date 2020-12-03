#!/usr/bin/env python3
import operator
import sys
from functools import reduce
from itertools import starmap, cycle, count, islice


def iterations_that_hit_trees_until_bottom(right_increment, down_increment):
    # get new hillside for each run, otherwise iterators maintain state
    hillside = [cycle(line.strip()) for line in open("../inputs/03_1.txt", "r")]
    return sum(
        list(islice(line, position - 1, position)) == ["#"]
        for line, position in zip(hillside[::down_increment], count(1, right_increment))
    )


def main():
    traversal_part_1 = (3, 1)
    traversals_part_2 = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    print(iterations_that_hit_trees_until_bottom(*traversal_part_1))
    print(
        reduce(
            operator.mul,
            starmap(iterations_that_hit_trees_until_bottom, traversals_part_2),
        )
    )


if __name__ == "__main__":
    sys.exit(main())
