import sys

T = int(sys.stdin.readline())

for tc in range(T):
    S = sys.stdin.readline()
    cnt = 0
    ans = []
    for i in range(len(S)):
        if S[i] == 'O':
            cnt += 1
            ans.append(cnt)
        elif S[i] == 'X':
            cnt = 0
    print(sum(ans))
