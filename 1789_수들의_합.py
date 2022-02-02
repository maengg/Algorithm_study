import sys

S = int(sys.stdin.readline())

n =1
# 1부터 n까지의 합이 S보다 커지면 n에서 1을 빼서 출력.
while (n*(n+1))/2 <= S:
    n +=1

print(n-1)