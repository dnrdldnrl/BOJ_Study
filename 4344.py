import sys

C = int(sys.stdin.readline())

for tc in range(C):
    input_info = list(map(int, sys.stdin.readline().split()))
    student = input_info[0]
    score = input_info[1:]
    avg = sum(score) / student
    over_avg_student = 0
    ans = 0
    for i in range(student):
        if score[i] > avg:
            over_avg_student += 1
        ans = (over_avg_student / student) * 100
    print("%.3f%%" % (ans))
