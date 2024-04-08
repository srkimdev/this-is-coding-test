import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
find_arr = list(map(int, input().split()))

def binary_find(arr, target, start, end):
    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return 'yes'

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1
    
    return 'no'

for i in find_arr:
    print(binary_find(arr, i, 0, n - 1), end = ' ')