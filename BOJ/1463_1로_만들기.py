import sys

n = int(sys.stdin.readline())

output = [0] * (n+1)

for i in range(2,n+1):
    # 이전 결과값을 활용 (-1의 연산을 했기에 +1)
    output[i] = output[i-1] + 1
    # 3과 2로 나눈 값의 결과를 재활용하는 것과 이전의 결과를 활용하는 것중에 최소연산을 활용
    if i%2 == 0:
        output[i] = min(output[i], output[i//2]+1)
    if i%3 == 0:
        output[i] = min(output[i], output[i//3]+1)

print(output[n])