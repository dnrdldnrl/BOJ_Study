import sys

T = int(sys.stdin.readline())

for tc in range(T):
    input_com = list(sys.stdin.readline().split())
    N = int(input_com[0])
    S = input_com[1]
    for i in range(len(S)):
        print(S[i] * N, end='')
    print()
