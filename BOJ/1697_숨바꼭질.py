import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

def bfs(queue):
    while queue:
        x = queue.popleft()
        # 동생 찾으면, 해당 위치 값 출력
        if x == k:
            print(graph[x])
            break
        for i in (x-1, x+1, x*2):
            # 이동한 위치가 0 이상 100,001 미만이고 해당 위치의 값이 0일때
            if 0 <= i < max and not graph[i]:
                # 1초씩 더해준다
                graph[i] = graph[x]+1
                queue.append(i)

# 범위가 0~10만 이라서 max값 100,001로 설정
max = 100001
graph = [0]*max
queue = deque([n])
bfs(queue)