from collections import deque

# queue를 이용한 bfs
# 다 순회하고 나온 결과값이 target과 같으면 answer + 1
def solution(numbers, target):
    answer = 0
    # idx가 list 길이와 같아지면 순회 끝.
    n = len(numbers)
    queue = deque([(0,0)])

    while queue:
        num, idx = queue.popleft()
        if idx < n:
            queue.append((num+numbers[idx], idx+1))
            queue.append((num-numbers[idx], idx+1))
        else:
            if num == target:
                answer += 1

    return answer