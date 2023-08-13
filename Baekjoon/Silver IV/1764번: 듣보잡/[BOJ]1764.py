import sys
input = sys.stdin.readline

#
# 1764번: 듣보잡
# https://www.acmicpc.net/problem/1764
#
# @author  Asher Seo
#

n, m = map(int, input().split())
A = [input().rstrip() for _ in range(n)]
B = [input().rstrip() for _ in range(m)]

res = sorted(list(set(A).intersection(B)))
print(len(res))
for ans in res:
  print(ans)
