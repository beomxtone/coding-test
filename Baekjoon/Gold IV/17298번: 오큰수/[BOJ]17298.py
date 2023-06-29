import sys
input = sys.stdin.readline

#
# 17298번: 오큰수
# https://www.acmicpc.net/problem/17298
#
# 1. 입력받은 수열의 index를 하나씩 스택에 삽입
# 2. 스택의 마지막 값과 삽입되는 수열의 값을 비교
# 3. 수열의 값이 마지막 값보다 작거나 같으면 그대로 스택에 넣고, 크다면 수열의 값보다 작은 값들을 모두 pop
# 4. 맨 마지막은 항상 -1
#
# @author  Asher Seo
#

n = int(input())
seq = list(map(int, input().split()))
stk = []
ans = [-1]*n

for i in range(n):
  # 스택의 마지막 값보다 현재 삽입한 값이 크면
  while stk and seq[stk[-1]] < seq[i]:
    idx = stk.pop()
    ans[idx] = seq[i]
  stk.append(i)
  
print(*ans)
