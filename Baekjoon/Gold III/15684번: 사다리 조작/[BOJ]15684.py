import sys
input = sys.stdin.readline

#
# 15684번: 사다리 조작
# https://www.acmicpc.net/problem/15684
#
# 1. i번 사다리가 i번 위치에 도달하는지 확인하는 함수를 만든다.
# 2. 사다리를 놓을 수 있는 위치에 놓으며, 1번 함수를 실행해 결과를 확인한다.
# 3. 2의 횟수의 최소값을 구하고, 불가능하면 -1, 3을 넘어가면 -1을 출력한다.
# 4. 가로선은 연속하거나 접할 수 없다.
#
# 해당 풀이는 4344ms가 나왔다.
# rows 배열을 Boolean으로 선언하고, check 함수의 while을 for문으로 변경하면 1700ms 정도 나온다.
#
# @author  Asher Seo
#

def check():
  for num in range(1, n):
    col = num
    idx = 1

    while idx <= h:
      row = rows[idx]
      # 가로선이 num+1 방향일 경우
      if col in row:
        col += 1
      # 가로선이 num-1 방향일 경우
      elif col-1 in row:
        col -= 1
      idx += 1

    # 최종 도착지점이 출발 지점과 다르면 False
    if num != col:
      return False
  
  return True

def ladder(depth, x, y):
  global ans
  if check():
    ans = min(ans, depth)
    return

  # 사다리를 3회 놓았거나, 정답보다 크면 다음 경우의 수를 찾음
  if depth >= 3 or depth >= ans:
    return

  for i in range(x, h+1):
    k = y if i == x else 0
    for j in range(k, n):
      if j not in rows[i] and j-1 not in rows[i] and j+1 not in rows[i]:
        rows[i].append(j)
        ladder(depth+1, i, j+2)
        rows[i].pop()


n, m, h = map(int, input().split())
rows = [[] for _ in range(h+1)]
ans = 10

# 사다리를 놓지 않고도 정답이면 0 출력 후 종료
if m == 0:
  print(0)
  exit()

for i in range(m):
  a, b = map(int, input().split())
  # a번 위치에 b, b+1번 세로선을 연결하는 가로선
  rows[a].append(b)

# 답이 3보다 크면 -1을 출력 (불가능하면 10이므로 -1 출력)
ladder(0, 1, 1)
print(ans if ans <= 3 else -1)
