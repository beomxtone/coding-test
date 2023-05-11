import sys
input = sys.stdin.readline

# 회의 시간을 (x, y)로 나타낸다고 가정
# 1. 회의 시간을 담은 배열에서 y의 값이 가장 작은 요소를 추출
# 2. 추출한 y의 값보다 큰 y값을 가진 요소가 배열 안에 없으면 종료

n = int(input())
meetings = []
for _ in range(n):
  meetings.append(tuple(map(int, input().split())))

meetings = sorted(meetings, key = lambda x : (x[1], x[0]))  # meetings 배열을 y가 작은 순서대로 정렬
currentMeet = (0, 0)  # 현재 회의의 시간 저장
cnt = 0
for meet in meetings:
  if meet[0] >= currentMeet[1]:
    currentMeet = meet
    cnt += 1

print(cnt)