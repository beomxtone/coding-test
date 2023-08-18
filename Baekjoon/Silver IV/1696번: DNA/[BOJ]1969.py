import sys
input = sys.stdin.readline

#
# 1969번: DNA
# https://www.acmicpc.net/problem/1969
#
# @author  Asher Seo
#

n, m = map(int, input().split())
dnaList = [input().rstrip() for _ in range(n)]

ans = ''
cnt = 0

for i in range(m):
  # A C G T, 사전 순
  dnas = [0, 0, 0, 0]
  for j in range(n):
    if dnaList[j][i] == 'A':
      dnas[0] += 1
    elif dnaList[j][i] == 'C':
      dnas[1] += 1
    elif dnaList[j][i] == 'G':
      dnas[2] += 1
    elif dnaList[j][i] == 'T':
      dnas[3] += 1

  resDna = dnas.index(max(dnas))

  if resDna == 0:
    ans += 'A'
  elif resDna == 1:
    ans += 'C'
  elif resDna == 2:
    ans += 'G'
  elif resDna == 3:
    ans += 'T'
    
  cnt += n - max(dnas)

print(ans)
print(cnt)
