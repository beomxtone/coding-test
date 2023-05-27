import sys
input = sys.stdin.readline

#
# 14888번: 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
#
# @author  Asher Seo
#

def addSign(count, value, plus, minus, multiply, divide):
  global maxNum, minNum
  if count == n:
    maxNum = max(maxNum, value)
    minNum = min(minNum, value)
    return

  if plus:
    addSign(count+1, value + nums[count], plus-1, minus, multiply, divide)
  if minus:
    addSign(count+1, value - nums[count], plus, minus-1, multiply, divide)
  if multiply:
    addSign(count+1, value * nums[count], plus, minus, multiply-1, divide)
  if divide:
    addSign(count+1, int(value / nums[count]), plus, minus, multiply, divide-1)

# n: 수의 개수
n = int(input())
# nums: n개의 수
nums = list(map(int, input().split()))
# signs: + - × ÷ 의 수
signs = list(map(int, input().split()))
maxNum = -1 * 10**9
minNum = 10**9

addSign(1, nums[0], signs[0], signs[1], signs[2], signs[3])
print(maxNum)
print(minNum)
