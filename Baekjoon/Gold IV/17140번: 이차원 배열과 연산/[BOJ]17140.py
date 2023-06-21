import sys
input = sys.stdin.readline

#
# 17140번: 이차원 배열과 연산
# https://www.acmicpc.net/problem/17140
#
# 1. arr[r][c]가 k이면 종료
# 2. 행과 열의 길이에 따라 r연산, c연산을 수행
# 3. 각 연산의 정렬 방식은 딕셔너리로 구현, 수의 등장 횟수가 커지는 순서, 같으면 수가 커지는 순서
#
# @author  Asher Seo

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

ans = 0
while ans < 101:
  if len(arr) > r-1 and len(arr[0]) > c-1:
    if arr[r-1][c-1] == k:
      break
  
  ans += 1
  rLn = len(arr)
  cLn = len(arr[0])

  if rLn >= cLn:
    # r연산 수행
    maxLen = 0
    for i in range(rLn):
      dic = {}
      
      for j in range(len(arr[i])):
        if arr[i][j] == 0: continue
        elif arr[i][j] not in dic:
          dic[arr[i][j]] = 1
        else:
          dic[arr[i][j]] += 1

      res = list(sum(sorted(dic.items(), key=lambda x:(x[1], x[0])), ()))
      arr[i] = res
      maxLen = max(maxLen, len(res))

    for i in range(rLn):
      for j in range(maxLen - len(arr[i])):
        arr[i].append(0)
    
  else:
    # c연산 수행
    maxLen = 0
    tmp = list(map(list, zip(*arr)))

    for i in range(len(tmp)):
      dic = {}

      for j in range(len(tmp[i])):
        if tmp[i][j] == 0: continue
        elif tmp[i][j] not in dic:
          dic[tmp[i][j]] = 1
        else:
          dic[tmp[i][j]] += 1

      res = list(sum(sorted(dic.items(), key=lambda x:(x[1], x[0])), ()))
      tmp[i] = res
      maxLen = max(maxLen, len(res))

    for i in range(len(tmp)):
      for j in range(maxLen - len(tmp[i])):
        tmp[i].append(0)

    arr = list(map(list, zip(*tmp)))

print(ans if ans != 101 else -1)
