li = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1 ,0 ,0 ,0 ,1 ,1 ,1 ,1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0 ,0 ,1 ,1 ,1 ,1 ,1 ,1],
    [0, 0, 1, 1, 1, 1, 1, 1]
]

mid = len(li)//2

paper1 = [paper[:mid] for paper in li[:mid]]
paper2 = [paper[mid:] for paper in li[:mid]]
paper3 = [paper[:mid] for paper in li[mid:]]
paper4 = [paper[mid:] for paper in li[mid:]]

print(paper1)
print(paper2)
print(paper3)
print(paper4)