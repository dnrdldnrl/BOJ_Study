import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = map(int, sys.stdin.readline().split())
A.sort()


def binarySearch(k, A, left, right):
    if left > right:
        return 0
    mid = (left+right)//2
    if k == A[mid]:
        return 1
    elif k < A[mid]:
        right = mid - 1
    else:
        left = mid + 1
    return binarySearch(k, A, left, right)


for k in M_list:
    left = 0
    right = len(A)-1
    print(binarySearch(k, A, left, right))
