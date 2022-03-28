def solution(array, commands):
    answer = []
    # 0번째 start, 1번째 end, 2번째 index -> [start-1:end][index]
    for li in commands:
        answer.append(sorted(array[li[0]-1:li[1]])[li[2]-1])
    return answer
