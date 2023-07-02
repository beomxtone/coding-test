import sys
input = sys.stdin.readline

#
# 6549번: 히스토그램에서 가장 큰 직사각형
# https://www.acmicpc.net/problem/6549
#
# 1. 히스토그램의 중간을 기준으로 한 칸이 될 때까지 나눈다.
# 2. 왼쪽, 오른쪽, 기준점을 합친 영역 중 큰 값을 선택하며 합친다.
# 3. 기준점을 포함한 영역은 두 개의 포인터를 양쪽으로 늘려나가며 가장 큰 직사각형을 구한다.
# 4. 2의 값 중 가장 큰 값을 재귀적으로 갱신하고 답을 출력
#
# @author  Asher Seo
#

def getMax(l, r):
  if l == r: return h[l]
    
  m = (l + r) // 2
  # 왼쪽과 오른쪽 영역 중 큰 값을 가져옴
  res = max(getMax(l, m), getMax(m+1, r))

  # 중간 점을 기준으로 왼쪽, 오른쪽으로 한칸씩 옮겨감
  lpos, rpos = m, m+1
  hgt = min(h[lpos], h[rpos])

  # 현재 비교하는 영역 안에서 비교
  while (lpos >= l and rpos <= r):
    hgt = min(hgt, h[lpos], h[rpos])
    res = max(res, hgt * (rpos - lpos + 1))

    if lpos == l: rpos += 1
    elif rpos == r: lpos -= 1
    # 왼쪽이나 오른쪽 중 큰 곳으로 영역을 넓히며 비교하기 때문에, 높이가 0인 경우는 고려하지 않아도 된다.
    elif h[rpos+1] >= h[lpos-1]: rpos += 1
    else: lpos -= 1
  
  return res


while True:
  histograms = list(map(int, input().split()))
  n = histograms[0]
  h = histograms[1:]

  if n == 0: break
  print(getMax(0, n-1))
