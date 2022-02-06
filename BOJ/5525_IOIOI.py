import sys

n = int(sys.stdin.readline())
str_length = int(sys.stdin.readline())
ioi_str = sys.stdin.readline()

cnt, idx, result = 0, 0, 0
# IOI 패턴을 찾으면 인덱스 2칸씩 움직이고 카운트 1 추가.
while idx < str_length-1:
    if ioi_str[idx:idx+3] == 'IOI':
        cnt += 1
        idx += 2
        # 카운트가 n이면 result에 1 추가하고 카운트는 -1
        if cnt == n:
            result += 1
            cnt -= 1
    # n이 2이상일때 중간에 패턴이 끊기면 cnt 0으로 초기화
    else:
        cnt = 0
        idx += 1
print(result)

### 50점 맞은 코드
# string find 메서드의 시간 복잡도는 최악의 경우 n -> 문자열의 길이, m -> 찾으려는 문자열의 길이 O(n*m)이라는데 확실하지 않아서 더 찾아봐야 함.
# import sys

# n = int(sys.stdin.readline())
# str_lengt = int(sys.stdin.readline())
# ioi_str = sys.stdin.readline()

# target = 'IO'*n+'I'
# idx = ioi_str.find(target)
# cnt = 0
# while idx != -1: -> 더이상 패턴이 없으면 반복 중단.
#     cnt += 1
#     ioi_str = ioi_str[idx+1:]
#     idx = ioi_str.find(target)
# print(cnt)