import sys
input = sys.stdin.readline

#
# 1253번: 좋다
# https://www.acmicpc.net/problem/1253
#
# 1. C를 만드는데 A와 B의 모든 경우를 검사하면 2000*2000으로 TLE 예상
# 2. 먼저 배열을 정렬(NlogN), A를 고르고(N) C를 만들 수 있는 B를 이분 탐색(logN)으로 찾는다. = NlogN
# 3. C를 만들 수 있는 B를 찾으면 정답에 1을 더한다.
#
# @author  Asher Seo
#

def binarySearch(start, end, target):
  global ans
  while start <= end:
    mid = (start + end) // 2
    
    if arr[mid] == target:
      ans += 1
      return True
  
    if arr[mid] > target:
      end = mid - 1
    
    else:
      start = mid + 1
    

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
for i in range(n):
  target = arr.pop(i)
  for j in range(n-2):
    num = arr.pop(j)
    
    if binarySearch(0, len(arr) - 1, target - num):
      arr.insert(j, num)
      break
    
    arr.insert(j, num)
  arr.insert(i, target)

print(ans)
