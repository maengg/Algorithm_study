import sys
from collections import deque

n, m , k = map(int, sys.stdin.readline().split())

# 그래프 생성
graph = [[False]*m for _ in range(n)]

for _ in range(k):
    a, b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = True

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    global count

    queue = deque([(x,y)])

    while queue:
        x, y = queue.popleft()
        graph[x][y] = False
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프 벗어나지 않는 조건.
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == True:
                    # 방문 처리로 바꿈.
                    graph[nx][ny] = False
                    queue.append((nx, ny))
                    count += 1

answer = 0
# 음식물 쓰레기가 하나라도 있으면 크기는 1
count = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == True:
            bfs(graph, i, j)
            # 둘 중 큰 값을 answer로 할당.
            answer = max(answer, count)
            count = 1

print(answer)