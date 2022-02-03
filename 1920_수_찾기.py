n = int(input())
# 이진 탐색은 정렬이 되어 있어야 사용 가능하기에 정렬해줌.
n_list = sorted(list(map(int, input().split(' '))))
m = int(input())
m_list = list(map(int, input().split(' ')))

# 이진탐색
def binary_search(arr, value):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == value:
            return 1
        # 가운데 인덱스의 값이 찾고자 하는 값 보다 크면, 최대 인덱스를 mid-1로 수정.
        elif arr[mid] > value:
            high = mid-1
        # 가운데 인덱스의 값이 찾고자 하는 값 보다 작거나 같다면, 최소 인덱스를 mid+1로 수정.    
        else:
            low = mid+1
    # 반복문을 빠져나왔다면, 값이 없는 것이기에 0을 반환.
    return 0

for value in m_list:
    print(binary_search(n_list, value))