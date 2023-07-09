for test_case in range(1,11):
    result = 0
    n = int(input())
    buildings = list(map(int , input().split()))
    
    for i in range(2, n-2):
        if buildings[i-2] > buildings[i] or buildings[i-1] > buildings[i] or buildings[i+1] > buildings[i] or buildings[i+2] > buildings[i]:
            continue
        result += buildings[i] - max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])

    print(f'#{test_case} {result}')
