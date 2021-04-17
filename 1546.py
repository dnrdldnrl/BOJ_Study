import sys
N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
max_score = max(l)
ans = 0

for i in range(len(l)):
    l[i] = (l[i] / max_score) * 100

ans = sum(l) / N

print(ans)
