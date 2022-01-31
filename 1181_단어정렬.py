n = int(input())
# set을 이용해서 중복을 제거하고 sorted의 key 인자에 lambda를 사용하여 정렬기준을 2가지로 설정했다.
words = sorted(list({input() for _ in range(n)}), key=lambda x : (len(x),x))
for i in words:
    print(i)