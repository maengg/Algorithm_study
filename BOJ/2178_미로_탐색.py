from collections import deque

n, m = map(int, input().split())

graph = [list(map(int,input())) for _ in range(n)]

# 좌, 우, 상, 하
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

queue = deque([(0,0)])

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 그래프 끝에 오면 출력하고 break
        if x == n-1 and y == m-1:
            print(graph[n-1][m-1])
            break
        
        # 그래프 벗어나면 안되는 조건
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                continue
            # 움직인 곳이 1 이면 그 전의 값 추가
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))