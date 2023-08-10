import sys
input = sys.stdin.readline

#
# 12850번: 본대 산책2
# https://www.acmicpc.net/problem/12850
#
# 1. a to b의 경우의 수는 인접 행렬의 거듭제곱과 같다.
# 2. D분 후에 시작 위치에 돌아와야 하므로, 인접 행렬의 D제곱에서 [0][0]을 (시작 위치) 구하면 된다.
# 3. 인접 행렬의 D제곱은 분할 정복을 이용해 구한다.
#
# @author  Asher Seo
#

p = 1000000007
maps = [
  [0, 1, 1, 0, 0, 0, 0, 0], # 정보과학관
  [1, 0, 1, 1, 0, 0, 0, 0], # 전산관
  [1, 1, 0, 1, 1, 0, 0, 0], # 미래관
  [0, 1, 1, 0, 1, 1, 0, 0], # 신양관
  [0, 0, 1, 1, 0, 1, 1, 0], # 한경직기념관
  [0, 0, 0, 1, 1, 0, 0, 1], # 진리관
  [0, 0, 0, 0, 1, 0, 0, 1], # 형남공학관
  [0, 0, 0, 0, 0, 1, 1, 0], # 학생회관
]

# 행렬의 곱
def multiply(a, b):
  res = [[0] * 8 for _ in range(8)]
  for i in range(8):
    for j in range(8):
      for k in range(8):
        res[i][j] += (a[i][k] * b[k][j]) % p
  return res

# 거듭 제곱의 분할 정복
def pow(mat, n):
  if n == 1:
    return mat
    
  tmp = pow(mat, n//2)
  if n % 2:
    return multiply(multiply(tmp, tmp), mat)
  else:
    return multiply(tmp, tmp)


D = int(input())
ans = pow(maps, D)
print(ans[0][0] % p)
