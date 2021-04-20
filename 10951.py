import sys

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
"""
EOF : End Of File 라는 뜻으로 파일의 끝을 의미한다. 10951 문제는 종결조건이 없으므로 계속 입력을 받으므로
예외처리문을 넣어주어 계속되는 입력에 EOF 에러가 뜨면 예외처리문으로 break 해주어 루프를 끝낸다.
"""
