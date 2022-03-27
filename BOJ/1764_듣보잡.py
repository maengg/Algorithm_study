n, m = map(int, input().split())

a = set()
for _ in range(n):
    a.add(input())

b = set()
for _ in range(m):
    b.add(input())

# set 교집합으로 중복된 이름을 리스트 형태로 만든다.
answer = sorted(list(a&b))

print(len(answer))
for name in answer:
    print(name)