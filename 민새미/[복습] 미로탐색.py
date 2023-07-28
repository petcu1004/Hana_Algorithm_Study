from collections import deque

n, m=map(int, input().split())
arr=list()
for i in range(n):
    k=list(map(int,input()))
    arr.append(k)

# print(arr)
dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]

def bfs(a, b):
    q=deque()
    q.append((a, b))
    while(q):
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if arr[nx][ny]==0:
                continue
            if arr[nx][ny]==1:
                q.append((nx, ny))
                arr[nx][ny]=arr[x][y]+1
    return arr[n-1][m-1]

print(bfs(0, 0))