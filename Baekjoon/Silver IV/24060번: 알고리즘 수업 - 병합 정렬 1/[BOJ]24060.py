import sys
input = sys.stdin.readline

#
# 24060번: 알고리즘 수업 - 병합 정렬 1
# https://www.acmicpc.net/problem/24060
#
# @author  Asher Seo
#

def mergeSort(L):
  if len(L) == 1:
    return L

  mid = (len(L) + 1) // 2
  left = mergeSort(L[:mid])
  right = mergeSort(L[mid:])
  
  i,j = 0, 0
  tmp = []
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      tmp.append(left[i])
      answer.append(left[i])
      i += 1
    else:
      tmp.append(right[j])
      answer.append(right[j])
      j += 1
  while i < len(left):
    tmp.append(left[i])
    answer.append(left[i])
    i += 1
  while j < len(right):
    tmp.append(right[j])
    answer.append(right[j])
    j += 1

  return tmp

n, k = map(int, input().split())
a = list(map(int, input().split()))
answer = []
mergeSort(a)

if len(answer) >= k:
  print(answer[k-1])
else:
  print(-1)
  