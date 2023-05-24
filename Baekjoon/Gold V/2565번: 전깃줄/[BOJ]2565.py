import sys
input = sys.stdin.readline

#
# 2565번: 전깃줄
# https://www.acmicpc.net/problem/2565
#
# 1. 전깃줄이 겹치지 않으려면 A에서 B로 증가하거나 감소하는 부분수열을 구하면 된다.
# 2. 전깃줄의 개수에서 LIS dp 배열의 최댓값을 뺀 값을 출력한다.
#
# @author  Asher Seo
#

# n: 전깃줄의 개수
n = int(input())
# L: 전깃줄의 정점을 저장하는 배열
L = []
# d: 전깃줄의 증가, 감소 수열의 길이를 구하는 DP 배열
d = [1]*n

for _ in range(n):
  a, b = map(int, input().split())
  L.append((a, b))
# A에서 시작하는 전깃줄을 오름차순으로 정렬
L = sorted(L, key=lambda x:(x[0], x[1]))

for i in range(n):
  for j in range(0, i):
    # 같은 위치에는 전깃줄이 연결될 수 없으므로 같은 조건은 없다
    if L[i][1] > L[j][1]:
      d[i] = max(d[i], d[j] + 1)
# 전깃줄의 갯수 - 겹치지 않는 최대 전깃줄의 수
print(n - max(d))
