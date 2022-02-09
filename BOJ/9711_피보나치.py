import sys

n = int(sys.stdin.readline())
test_case = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def max_num(test_case):
    nums_list = [nums[0] for nums in test_case]
    return max(nums_list)

def fibo(num):
    output = [0,1]
    for i in range(2,num+1):
        output.append(output[i-1] + output[i-2])
    return output

max_n = max_num(test_case)
output = fibo(max_n)
for i in range(0,len(test_case)):
    print(f'Case #{i+1}: {(output[test_case[i][0]]%test_case[i][1])}')