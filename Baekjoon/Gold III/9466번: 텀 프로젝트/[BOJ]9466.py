import sys
input = sys.stdin.readline

#
# 9466번: 텀 프로젝트
# https://www.acmicpc.net/problem/9466
#
# 1. index를 1씩 증가시킨다.
# 2. cycle이 만들어지면 해당 index의 요소를 0으로 변경한다.
# 3. 0이면 스킵하며 전부 탐색한 후 0이 아닌 index의 수를 리턴한다.
# 4. 이미 방문했으면 -1로 설정
#
# @author  Asher Seo
#

t = int(input())
for _ in range(t):
  n = int(input())
  students = [0] + list(map(int, input().split()))
  visited = {}
  ans = 0
  
  for i in range(1, n+1):
    if i not in visited:
      team = [students[i]]
      team_set = set()
      team_set.add(students[i])

      while True:
        curr = team[-1]
        next = students[curr]

        if curr in visited: break
        visited[curr] = True

        if next in team_set:
          target_index = team.index(next)
          for j in range(target_index, len(team)):
            target = team[j]
            students[target] = 0
          break

        team.append(next)
        team_set.add(next)

      visited[i] = True

  for i in range(1, n+1):
    if students[i]: ans += 1
  print(ans)
