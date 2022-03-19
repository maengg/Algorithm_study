from collections import deque

def solution(n, computers):
    answer = 0

    # 모든 컴퓨터 확인을 위해 visited=[], 말고 False로 만들어 놓고 True로 바꾸는 방식 선택.
    visited = [False for _ in range(n)]

    # 연결이 끊어져도 모든 컴퓨터의 네트워크를 다 확인해야 함.
    while visited.count(False) != 0:
        node = visited.index(False)
        queue = deque([node])

        # bfs
        while queue:
            cur_node = queue.popleft()
            if visited[cur_node] is False:
                visited[cur_node] = True
                for i in range(n):
                    if computers[cur_node][i] != 0:
                        queue.append(i)
        # 연결된 컴퓨터 다 돌면 +1
        answer += 1
    
    return answer