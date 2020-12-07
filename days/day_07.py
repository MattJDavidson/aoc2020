#!/usr/bin/env python3
import re
import sys
from collections import defaultdict
from typing import List, Dict, Set, Tuple

Colour = str
QuantityOfColour = Tuple[int, Colour]
ParentsMap = Dict[Colour, Set]
ChildrenMap = Dict[Colour, List[QuantityOfColour]]


def find_parents(colour: Colour, parents: ParentsMap, found_parents: Set[Colour]):
    for parent in parents[colour]:
        found_parents.add(parent)
        find_parents(parent, parents, found_parents)


def count_bags(colour: Colour, children: ChildrenMap) -> int:
    return sum(map(lambda k: k[0] * (count_bags(k[1], children) + 1), children[colour]))


def hash_parents_and_children_lookups(lines: List[str],) -> (ParentsMap, ChildrenMap):
    parents_map: ParentsMap = defaultdict(set)
    children_map: ChildrenMap = defaultdict(list)
    for line in lines:
        parent_colour = re.match(r"(.+?) bags contain", line)[1]
        for num, child_colour in re.findall(r"(\d+) (.+?) bags?[,.]", line):
            parents_map[child_colour].add(parent_colour)
            children_map[parent_colour].append((int(num), child_colour))
    return parents_map, children_map


def main():
    lines = [line.strip() for line in open("../inputs/07_01.txt", "r")]
    parents, children = hash_parents_and_children_lookups(lines)

    golden_parents = set()
    find_parents("shiny gold", parents, golden_parents)
    print(len(golden_parents))

    print(count_bags("shiny gold", children))


if __name__ == "__main__":
    sys.exit(main())
