import sys

N, X = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))
ans = []

for i in range(N):
    if l[i] < X:
        ans.append(l[i])

for i in ans:
    print(i, end=" ")
