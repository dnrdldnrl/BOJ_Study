import sys

A, B = sys.stdin.readline().rstrip().split()
rev_A = A[::-1]
rev_B = B[::-1]

ans_A = int(rev_A)
ans_B = int(rev_B)

if ans_A > ans_B:
    print(ans_A)
else:
    print(ans_B)

# 시행착오 : 직접 for문으로 문자열을 역행으로 만드는데 까진 성공, 근데 정수로 변환할떄 Type Error가 남
# 해결방법 : 리스트를 역행으로 재배치 해주는 [::-1] 방법이 있었음.
# 미해결 : 입력을 받고 나서 바로 int형으로 캐스팅하면 int형으로 잘 변환이 되는데, for문을 사용해 역행 리스트를 만들고 int형으로 캐스팅할때 왜 TypeError가 뜨는지
