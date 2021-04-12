import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

print(min(l), max(l))


"""
import sys

l = []

for i in range(9):
    l.append(int(sys.stdin.readline()))

for i in range(len(l)):
    if l[i] == max(l):
        print(l[i])
        print(i+1)

"""
