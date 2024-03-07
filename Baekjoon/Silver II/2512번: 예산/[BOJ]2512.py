import sys
input = sys.stdin.readline

#
# 2512번: 예산
# https://www.acmicpc.net/problem/2512
#
# 1. 상한액 = 구하고자 하는 target
# 2. start = 0, end = 예산 최고액
# 3. mid로 구한 상한액으로 예산 책정했을 때, 초과하면 end를 mid-1로, 아니면 start를 mid+1로
#
# @author  Asher Seo
#

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

ans = 0
start, end = 0, max(budgets)

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    for budget in budgets:
        if budget > mid:
            total += mid
            continue
        total += budget

    if total <= m:
        ans = mid
        start = mid + 1
        continue
    
    end = mid - 1

print(ans)
