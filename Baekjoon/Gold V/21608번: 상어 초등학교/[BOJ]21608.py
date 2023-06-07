import sys
input = sys.stdin.readline

#
# 21608번: 상어 초등학교
# https://www.acmicpc.net/problem/21608
#
# 1. 학생 = index, 좋아하는 학생 = list의 원소로 구현
# 2. 첫 학생은 2번, 3번 조건에 따라 항상 (1, 1)에 위치한다.
# 3. 주어진 문제의 조건에 따라 구현
#
# @author  Asher Seo
#

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
fav = [[] for _ in range(n**2+1)]
seq = []
cls = [[0]*n for _ in range(n)]

for _ in range(n**2):
  a, b, c, d, e = map(int, input().split())
  seq.append(a)
  fav[a] = [b, c, d, e]

# 첫 학생을 (1, 1)에 배치
cls[1][1] = seq[0]
seq.pop(0)

# 나머지 자리 배치
for num in seq:
  x, y, likes, blanks = 0, 0, 0, 0
  
  for i in range(n):
    for j in range(n):
      
      if cls[i][j] == 0:
        likCnt, blkCnt = 0, 0

        # 상하좌우에 좋아하는 학생 수와 빈칸을 기록
        for k in range(4):
          if 0 <= i+dx[k] < n and 0 <= j+dy[k] < n:
            if cls[i+dx[k]][j+dy[k]] in fav[num]:
              likCnt += 1
            elif cls[i+dx[k]][j+dy[k]] == 0:
              blkCnt += 1

        # 해당 자리가 좋아하는 사람 수는 같지만 빈칸이 많은 경우 업데이트
        if likCnt == likes:
          if blkCnt > blanks:
            likes, blanks = likCnt, blkCnt
            x, y = i, j

        # 해당 자리가 좋아하는 사람 수가 많으면 업데이트
        elif likCnt > likes:
          likes, blanks = likCnt, blkCnt
          x, y = i, j

  # 자리가 비어있으면 해당 자리로 배정
  if cls[x][y] == 0:
    cls[x][y] = num
  # 자리가 이미 있으면 빈 자리를 찾음
  else:
    flag = 1
    for i in range(n):
      for j in range(n):
        if flag and cls[i][j] == 0:
          cls[i][j] = num
          flag = 0

# 만족도 구하기
ans = 0
for i in range(n):
  for j in range(n):
    stu = cls[i][j]
    cnt = 0
    
    for k in range(4):
      if 0 <= i+dx[k] < n and 0 <= j+dy[k] < n:
        if cls[i+dx[k]][j+dy[k]] in fav[stu]:
          cnt += 1

    if cnt != 0:
      ans += 10**(cnt-1)

print(ans)
