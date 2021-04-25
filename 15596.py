import sys


def solve(a):
    return sum(a)


a = list(map(int, sys.stdin.readline().split()))

print(solve(a))
