import sys

n = int(sys.stdin.readline())
test_case = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# test_case에서 구해야 하는 최대 p번째 숫자를 구하는 함수.
def max_num(test_case):
    nums_list = [nums[0] for nums in test_case]
    return max(nums_list)

# 피보나치 수열 리스트를 반환하는 함수
def fibo(num):
    output = [0,1]
    for i in range(2,num+1):
        output.append(output[i-1] + output[i-2])
    return output

# 피보나치 수열을 case 별로 계속 구하는 것이 아니라 최대 p번째 숫자까지 피보나치 수열을 구함.
# 이후 구해놓은 리스트를 바탕으로 나누기를 한다.
max_n = max_num(test_case)
output = fibo(max_n)
for i in range(0,len(test_case)):
    print(f'Case #{i+1}: {(output[test_case[i][0]]%test_case[i][1])}')