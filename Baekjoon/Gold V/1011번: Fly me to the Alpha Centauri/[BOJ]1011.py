import sys
input = sys.stdin.readline

#
# 1011번: Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011
#
# 1. 마지막은 1이 되어야 하므로, 중간 지점에서 가장 빠르고, 도착 지점은 1까지 감속해야 한다.
# 2. ex) 1 2 3 3 2 1,  1 2 3 4 5 4 3 2 1 ...
#
# @author  Asher Seo
#

T = int(input())
for _ in range(T):
  x, y = map(int, input().split())
  dis = y - x
  cur, tmp, ans = 0, 1, 0

  while cur < dis:
    ans += 1
    cur += tmp
    if ans % 2 == 0: tmp += 1

  print(ans)
