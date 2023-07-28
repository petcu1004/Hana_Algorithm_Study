from collections import deque

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input())))

# print(arr)

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def bfs(a, b):
    q=deque()
    k=1
    q.append((a, b))
    arr[a][b]=0 #이거 안써주면 틀림!!!!
    while q:
        x, y =q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if arr[nx][ny]==0:
                continue
            if arr[nx][ny]==1:
                arr[nx][ny]=0

                q.append((nx, ny))
                k+=1
    return k

res=list()
cnt=0
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            
            res.append(bfs(i, j))

print(len(res))
for i in sorted(res):
    print(i)