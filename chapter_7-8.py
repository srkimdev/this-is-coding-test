import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
rice_cake = list(map(int, input().split()))

start = 0
end = max(rice_cake)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in rice_cake:
        if i - mid > 0:
            total += i - mid

    if total >= m:
        start = mid + 1
        result = mid
    
    elif total < m:
        end = mid - 1

print(result)
