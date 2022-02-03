def solution(numbers):
    # 3, 34인 경우 334 < 343이 더 큼. 이렇게 잘못 정렬되는 걸 방지하기 위해 *3해서 정렬. (정수 범위 1,000까지니까)
    str_list = sorted(list(map(lambda x : str(x)*3, numbers)),reverse=True)    
    answer = ''
    for num in str_list:
        # 더할땐 str길이 3으로 나눈 만큼만 슬라이싱해서 (66 => 666666 => 66으로 바꾸는 과정)
        answer += num[:len(num)//3]
    # '0000'의 경우 0으로 출력되야 하기에 int로 변환 후 다시 str로 변환.
    answer = str(int(answer))
    
    return answer