def dfs(count):
    global answer
    if count == 0:
        result = int(''.join(nums))
        answer = max(answer, result)
        return
    for i in range(length):
        for j in range(i+1, length):
            nums[i], nums[j] = nums[j], nums[i]
            changed = ''.join(nums)
            if visited.get((changed, count-1), 1):
                visited[(changed, count-1)] = 0
                dfs(count-1)
            nums[i], nums[j] = nums[j], nums[i]

TC = int(input())
for T in range(1, TC+1):
    num, cnt = map(int, input().split())
    length = len(str(num))
    nums = list(str(num))
    answer = 0
    visited = {}
    dfs(cnt)
    print(f'#{T} {answer}')
