import sys

S = sys.stdin.readline()

# 아스키코드 ( a ~ z => 97 ~ 122 )

for i in range(97, 123):
    print(S.find(chr(i)), end=" ")
