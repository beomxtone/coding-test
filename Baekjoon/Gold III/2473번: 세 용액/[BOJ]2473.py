import sys
input = sys.stdin.readline

#
# 2473번: 세 용액
# https://www.acmicpc.net/problem/2473
#
# 1. 두 가지 용액을 합한 집합을 생성한다.
# 2. x+y+z가 0에 가까워야하므로, x+y가 -z에 가까우면 된다.
# 3. 1의 값이 -z에 가까운 값을 이분 탐색으로 찾고, 정답을 갱신한다.
#
# @author  Asher Seo
#

n = int(input())
liquids = sorted(list(map(int, input().split())))

minVal = 10**10
ans = [None, None, None]

for i in range(n - 1):
    for j in range(i + 1, n):
        x, y = liquids[i], liquids[j]
        start = j + 1
        end = n - 1

        while start <= end:
            mid = (start + end) // 2
            z = liquids[mid]
            val = x + y + z
            
            if minVal > abs(val):
                minVal = abs(val)
                ans = [x, y, z]

            if val > 0:
                end = mid - 1
            else:
                start = mid + 1

print(*ans)
