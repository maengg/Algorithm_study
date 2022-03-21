import sys

# 에리스토스테네스의 체
n, m = map(int, sys.stdin.readline().split())

arr = [False, False] + [True]*(m-1)

for i in range(2,m+1):
    # True인 경우 배수 제거.
    if arr[i]:
        for j in range(2*i, m+1, i):
            arr[j] = False
        if i >= n:
            print(i)
