count = 0

def dfs (numbers, idx, cur, target):
    global count
    if idx == len(numbers):
        if cur == target:
            count += 1
        return
    
    dfs(numbers, idx + 1, cur + numbers[idx], target)
    dfs(numbers, idx + 1, cur - numbers[idx], target)
    
    return

def solution(numbers, target):
    dfs(numbers, 0, 0, target)
    return count