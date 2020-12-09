#!/usr/bin/env python
import itertools
import os
import sys
from collections import deque
from io import BytesIO, IOBase


def main():
    preamble_length = 25
    previous_numbers = [input() for _ in range(preamble_length)]

    new_number = input()
    target = 0
    while new_number:
        if not any(
            (x + y) == new_number
            for x, y in itertools.combinations(previous_numbers[-preamble_length:], 2)
        ):
            target = new_number
            break

        previous_numbers.append(new_number)
        new_number = input()

    print(target)

    current_range = deque()

    numbers = iter(previous_numbers)
    while sum(current_range) != target or not current_range:
        current_range.append(next(numbers)) if sum(
            current_range
        ) < target else current_range.popleft()

    print(sum((min(current_range), max(current_range))))


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: int(sys.stdin.readline().rstrip("\r\n"))

# endregion

if __name__ == "__main__":
    main()
