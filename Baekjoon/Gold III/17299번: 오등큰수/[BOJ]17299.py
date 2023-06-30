import sys
input = sys.stdin.readline

#
# 17299번: 오등큰수
# https://www.acmicpc.net/problem/17299
#
# 1. dictionary를 사용해 수열의 원소를 count
# 2. 입력받은 수열의 index를 하나씩 스택에 삽입
# 3. 스택의 마지막 값과 삽입되는 수열의 값을 비교
# 4. 수열의 값이 마지막 값보다 작거나 같으면 그대로 스택에 넣고, 크다면 수열의 값보다 작은 값들을 모두 pop
#
# @author  Asher Seo
#

n = int(input())
seq = list(map(int, input().split()))
stk = []
ans = [-1]*n
dict = {}

for s in seq:
  if s in dict:
    dict[s] += 1
  else:
    dict[s] = 1

for i in range(n):
  # 스택의 마지막 값보다 현재 삽입한 값이 크면
  while stk and dict[seq[stk[-1]]] < dict[seq[i]]:
    idx = stk.pop()
    ans[idx] = seq[i]
  stk.append(i)
  
print(*ans)
