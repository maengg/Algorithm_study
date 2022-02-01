import sys

n = int(sys.stdin.readline())
# 2차 리스트로 생성
papers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def count_paper(li):
    length = len(li)
    mid = length//2
    # list의 모든 요소가 1일 경우 그 합은 length*length => 이 경우 1을 추가
    if sum(list(map(sum, li))) == length*length: 
        output.append(1)
    # list의 모든 요소가 0일 경우 그 합은 0 => 이 경우 0을 추가
    elif sum(list(map(sum, li))) == 0:
        output.append(0)
    # 리스트를 4등분 하는 과정
    else:
        paper1 = [paper[:mid] for paper in li[:mid]]
        paper2 = [paper[mid:] for paper in li[:mid]]
        paper3 = [paper[:mid] for paper in li[mid:]]
        paper4 = [paper[mid:] for paper in li[mid:]]
        
        count_paper(paper1)
        count_paper(paper2)
        count_paper(paper3)
        count_paper(paper4)

        return output
    
    
output = []
count_paper(papers)
print(output.count(0))
print(output.count(1))