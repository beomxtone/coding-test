import sys
input = sys.stdin.readline

#
# 9527번: 1의 개수 세기
# https://www.acmicpc.net/problem/9527
#
# 1. 1~B 까지의 1의 개수 - 1~(A-1)까지의 1의 개수로 답을 구한다. => fn(B) - fn(A-1)
# 2. 2^n - 1 까지의 1의 개수는 1, 4, 12, 32, 80 ... => d[n] = 2*d[n-1] + 2^(n-1)
# 3. 2^n - 1을 넘어가는 경우, 넘어간 부분의 맨 앞의 1을 모두 센다. (13이면 13-8+1)
# 4. 그 후 남은 부분의 1을 세는데, 이는 3의 2^n - 1에서의 남은 부분을 세는 것과 동일하다. (13이면 5와 같다.)
# 5. 3-4의 과정을 반복하고 1의 과정을 통해 정답을 출력한다.
#
# @author  Asher Seo
#

def count(n):
  binary = bin(n)[2:]
  res = 0

  for i in range(len(binary)):
    # python의 경우, '0'도 true
    if binary[i] == '1':
      power = len(binary)- i - 1
      # 10111(2)의 경우, 10000(2) 까지의 1의 개수를 더함
      res += d[power]
      # 13의 경우, 8 뒤로 8 9 10 11 12 13(총 6개 = 13-(2**3)+1) 맨 앞 1의 개수를 더함
      res += n - 2**power + 1
      # 13의 경우, 위의 과정을 마치면 5의 1의 개수를 세는 문제가 된다. => 13 - 2**3
      n = n - 2**power
  
  return res


A, B = map(int, input().split())
# 10^16까지의 2^n - 1 일 때의 1의 개수
d = [0] * 55

for i in range(1, 55):
  d[i] = 2*d[i-1] + 2**(i-1)

print(count(B) - count(A-1))
