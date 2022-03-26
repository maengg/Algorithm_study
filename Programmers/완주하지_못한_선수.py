def solution(participant, completion):
    dict = {}
    temp = 0
    for name in participant:
        # 해시 값을 key로 이름을 value로
        dict[hash(name)] = name
        # 해시 값을 더한다.
        temp += hash(name)
    for name in completion:
        # 완주자 해시 값을 뺀다. -> 완주하지 못한 해시값만 남는다.
        temp -= hash(name)
    answer = dict[temp]
    return answer
