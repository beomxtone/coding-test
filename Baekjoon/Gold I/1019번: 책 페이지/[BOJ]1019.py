import sys
input = sys.stdin.readline

#
# 1019번: 책 페이지
# https://www.acmicpc.net/problem/1019
#
# 1. 책 페이지를 하나하나 세면, 10억 제한에 TLE
# 2. A와 B 사이의 수를 세는 문제로 바꾼다. (A의 일의 자리 0, B의 일의 자리 9)
# 3. A의 일의 자리와 B의 일의 자리를 0과 9로 맞추고, 맞추는 과정에서 정답 배열을 갱신한다.
# 4. 앞이 0, 뒤가 9이면 0~9는 (B/10 - A/10 + 1) * digit번 등장한다.
# 5. A가 B와 같아질 때까지 자리 수를 바꿔가며 반복, 정답을 출력한다.
#
# @author  Asher Seo
#

# 수 N이 어떤 수로 이루어져 있는지 구하는 함수 (5454는 5가 2개, 4가 2개)
def calc(n, digit):
  while n > 0:
    # A와 B를 0과 9로 맞추는 과정에서, 각각의 자리수 만큼 0~9가 등장한다.
    ans[n%10] += digit
    n //= 10

def solve(A, B, digit):
  # A의 일의 자리 수를 0으로 맞춘다.
  while A%10 and A <= B:
    calc(A, digit)
    A += 1

  if A > B: return

  # B의 일의 자리 수를 9로 맞춘다.
  while B%10 != 9 and B >= A:
    calc(B, digit)
    B -= 1

  # A의 일의자리가 0, B의 일의자리가 9이면 각 숫자는 (B//10 - A//10 + 1) * digit번 등장한다.
  count = B//10 - A//10 + 1
  for i in range(10):
    ans[i] += count * digit

  # 다음 자리 수 진행
  solve(A//10, B//10, digit*10)


N = int(input())
ans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

solve(1, N, 1)
print(*ans)
