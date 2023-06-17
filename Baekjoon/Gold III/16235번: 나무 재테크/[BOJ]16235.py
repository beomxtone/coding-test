import sys
input = sys.stdin.readline

#
# 16235번: 나무 재테크
# https://www.acmicpc.net/problem/16235
#
# 1. 토지 양분값을 5로 초기화, 나무 여러 그루를 나타낼 수 있는 나무 배열: [x][y][trees]
# 2. 나무는 나이가 어린 순서대로 자신의 나이만큼 양분을 먹고 나이가 1 증가한다. (봄)
# 3. 양분을 먹지못해 죽은 나무는 (나이//2) 만큼 해당 칸에 양분으로 추가된다. (여름)
# 4. 나무의 나이가 5의 배수이면 인접 8칸에 나이 1인 나무를 생성 (가을)
# 5. 입력으로 받은 양분만큼 토지에 양분을 추가한다. (겨울)
# 6. k년 만큼 2~5를 반복하고, 남은 나무의 수를 세서 출력한다.
#
# @author  Asher Seo
#

n, m, k = map(int, input().split())
# nuts: 매년 겨울마다 뿌리는 양분의 정보
nuts = [list(map(int, input().split())) for _ in range(n)]
# graph: 토지의 양분이 얼마나 남았는지 나타내는 배열
graph = [[5 for _ in range(n)] for _ in range(n)]
# n은 최대 10이니까, 2차원 배열로 전부 검색해도 최대 10만번
trees = [[[] for _ in range(n)] for _ in range(n)]

# 입력한 나무의 정보를 추가
for _ in range(m):
  x, y, age = map(int, input().split())
  trees[x-1][y-1].append(age)

for _ in range(k):
  dead, fives = [], []
  # 봄: 나무는 양분을 먹고 성장
  for i in range(n):
    for j in range(n):
      # 해당 칸에 나무가 있으면
      if trees[i][j]:
        # 나무의 나이가 적은 순서대로
        trees[i][j].sort()
        # 죽은 나무의 인덱스
        temp = []
        
        for t in range(len(trees[i][j])):
          # 현재 토지에 충분한 양분이 남아있으면 나무가 성장
          if graph[i][j] >= trees[i][j][t]:
            graph[i][j] -= trees[i][j][t]
            trees[i][j][t] += 1
            # 나이가 5의 배수가 되면 번식 준비
            if trees[i][j][t] % 5 == 0:
              fives.append((i, j))
          # 현재 토지에 양분이 부족하면 나무는 죽음
          else:
            temp.append(t)
            dead.append((i, j, trees[i][j][t]))

        # 죽은 나무를 나무 배열에서 제거
        for t in temp:
          trees[i][j][t] = -1
        trees[i][j] = [t for t in trees[i][j] if t != -1]

  # 여름: 죽은 나무는 나이의 절반만큼 토지에 양분 추가
  for d in dead:
    x, y, nut = d[0], d[1], d[2]//2
    graph[x][y] += nut

  # 가을: 5의 배수인 나무는 주변 8칸에 번식
  for five in fives:
    x, y = five[0], five[1]

    if 0<=x+1<n and 0<=y<n:
      trees[x+1][y].append(1)
    if 0<=x<n and 0<=y+1<n:
      trees[x][y+1].append(1)
    if 0<=x-1<n and 0<=y<n:
      trees[x-1][y].append(1)
    if 0<=x<n and 0<=y-1<n:
      trees[x][y-1].append(1)
    if 0<=x+1<n and 0<=y+1<n:
      trees[x+1][y+1].append(1)
    if 0<=x+1<n and 0<=y-1<n:
      trees[x+1][y-1].append(1)
    if 0<=x-1<n and 0<=y+1<n:
      trees[x-1][y+1].append(1)
    if 0<=x-1<n and 0<=y-1<n:
      trees[x-1][y-1].append(1)

  # 겨울: 입력의 양분만큼 토지에 양분 추가
  for i in range(n):
    for j in range(n):
      graph[i][j] += nuts[i][j]

# 나무의 개수를 세서 답 출력
ans = 0
for i in range(n):
  for j in range(n):
    ans += len(trees[i][j])
print(ans)
