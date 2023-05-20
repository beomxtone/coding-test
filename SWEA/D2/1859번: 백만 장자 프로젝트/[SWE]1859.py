T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    L = list(map(int, input().split()))
    money, highest = 0, L[-1]
     
    for price in L[::-1]:
        if highest > price:
            money += highest - price
        else:
            highest = price
         
    print(f'#{test_case} {money}')
