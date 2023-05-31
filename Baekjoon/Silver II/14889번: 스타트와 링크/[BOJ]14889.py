import sys
input = sys.stdin.readline

#
# 14889번: 스타트와 링크
# https://www.acmicpc.net/problem/14889
#
# 1. 두 팀으로 나눌 수 있는 경우의 수를 모두 구한다.
# 2. 1에서 구한 두 팀의 능력치 차이의 최솟값이 정답이 된다.
#
# @author  Asher Seo
#

def calc():
  # team2: 모든 사람 - team1에 속한 사람
  team2 = [x for x in range(1, n+1) if x not in team1]
  stat1, stat2 = 0, 0
  
  for i in range(n//2):
    for j in range(n//2):
      if i != j:
        stat1 += stats[team1[i]-1][team1[j]-1]
        stat2 += stats[team2[i]-1][team2[j]-1]
  # 각팀 능력치 차이를 리턴
  return abs(stat1 - stat2)

def check(count):
  if count == n//2:
    global answer
    answer = min(answer, calc())
    return
  # 팀을 나누는 과정
  for i in range(2, n+1):
    # 중복이거나, 이전에 골랐던 경우는 제외
    if i not in team1 and team1[-1] < i:
      team1.append(i)
      check(count+1)
      team1.pop()

n = int(input())
stats = []
for _ in range(n):
  stats.append(list(map(int, input().split())))

team1 = [1]
answer = 10**9

check(1)
print(answer)
