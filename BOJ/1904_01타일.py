import sys
# 그림을 그려보니 피보나치 수열이란 걸 알았다.
n = int(sys.stdin.readline())

# 곱하기 n을 하면 n이 1이거나 2일때 밑에 output[1], output[2]를 정해준 곳에서 IndexError가 뜬다.
output=[0]*1000001
output[1]=1
output[2]=2
for i in range(3,n+1):
    output[i] = (output[i-1] + output[i-2])%15746 # 메모리 초과때문에 리스트에 넣을때 나눠줘야 한다.
print(output[n])