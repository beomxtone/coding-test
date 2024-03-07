import sys
input = sys.stdin.readline

#
# 2467번: 용액
# https://www.acmicpc.net/problem/2467
#
# 1. 용액들의 배열을 순차적으로 탐색
# 2. 용액과 다른 용액의 합이 정답보다 0에 가까우면 정답을 갱신
# 3. 2는 이분 탐색으로 구현
#
# @author  Asher Seo
#

n = int(input())
liquids = list(map(int, input().split()))

ansValue = 10**10
ans = [None, None]

for i in range(n-1):
    start = i+1
    end = n-1

    while start <= end:
        mid = (start + end) // 2
        val = liquids[i] + liquids[mid]
        
        if abs(val) < ansValue:
            ansValue = abs(val)
            ans = [liquids[i], liquids[mid]]

        if val < 0:
            start = mid + 1        
        else:
            end = mid - 1

print(*sorted(ans))
