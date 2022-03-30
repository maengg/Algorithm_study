from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    queue_plus = deque(speeds)
    answer = []
    count = 0
    while queue:
        # 첫번째 기능이 완료되면 기능과 스피드 큐 모두 popleft 후 count +1
        if queue[0] >= 100:
            queue.popleft()
            queue_plus.popleft()
            count += 1
            continue
        else:
            # 첫번째 기능이 완료가 되지 않았는데 count가 0 이상이라면 answer에 추가
            if count > 0 :
                answer.append(count)
                count = 0
            # 기능에 스피드 더하면서 개발 진행.
            for i in range(len(queue_plus)):
                queue[i] += queue_plus[i]
    # continue를 사용하였기에 count가 0이 아닌 경우에는 answer에 추가
    if count > 0:
        answer.append(count)
    return answer