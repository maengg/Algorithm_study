import sys
A, B = map(int, sys.stdin.readline().split())

result = []
# 수열 만들기
for i in range(B+1):
    for j in range(i):
        # 수열의 길이가 B보다 커지면 반복문 중단.
        if len(result) > B:
            break
        result.append(i)
# 리스트 슬라이싱 사용하여 합 구하기.
print(sum(result[A-1:B]))