import sys

l = []

for i in range(10):
    l.append(int(sys.stdin.readline()) % 42)

ans = set(l)
print(len(ans))

# set 함수는 중복되는 배열 인덱스를 하나로 제거해준다.
