import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[x][y] = True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
while True:
    turn = 0

    for i in range(1, 5):
        d = (d + i) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        turn += 1

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            x, y = nx, ny
            count += 1
            break
    
    if turn == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if graph[nx][ny] == 1:
            print(count)
            break
        else:
            x, y = nx, ny