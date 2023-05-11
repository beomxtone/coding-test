import sys
input = sys.stdin.readline

#
# 1874번: 스택 수열
# https://www.acmicpc.net/problem/1874
#
# 1. seq[seqIdx] 값까지 num값을 스택에 push한다.
# 2. seq[seqIdx] 값이 num보다 작으면 pop 하고, pop한 값이 seq[seqIdx] 값과 다르면 no를 출력한다.
#
# @author  Asher Seo
#

n = int(input())
seq, stack = [], []
seqIdx, num = 0, 1
answer = ''

for _ in range(n):
  seq.append(int(input()))

for _ in range(n*2):
  if seq[seqIdx] >= num:
    stack.append(num)
    num += 1
    answer += '+'
  else:
    try:
      popValue = stack.pop()
      if popValue == seq[seqIdx]:
        seqIdx += 1
        answer += '-'
      else:
        answer = 'NO'
        break
    except:
      answer = 'NO'
      break
if answer == 'NO': print(answer)
else: print(*list(answer), sep='\n')