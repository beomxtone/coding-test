import sys
input = sys.stdin.readline

#
# 1725번: 히스토그램
# https://www.acmicpc.net/problem/1725
#
# 1. 분할정복 대신 스택으로 풀이
# 2. 이전 높이 이상이면 스택에 index를 push, 낮으면 해당 점을 기준으로 가장 큰 직사각형을 구한다.
# 3. 2는 스택에서 하나씩 pop하면서, 스택이 비거나 기준 점보다 작아질 때까지 반복한다.
#
# @author  Asher Seo
#

n = int(input())
h = [int(input()) for _ in range(n)]
stk = [0]
ans = 0

for i in range(1, n):
  while stk and h[stk[-1]] > h[i]:
    hgt = h[stk.pop()]
    wid = i - stk[-1] - 1 if stk else i
    ans = max(ans, hgt * wid)
  stk.append(i)

while stk:
  hgt = h[stk.pop()]
  wid = n if not stk else n - stk[-1] - 1
  ans = max(ans, hgt*wid)

print(ans)
