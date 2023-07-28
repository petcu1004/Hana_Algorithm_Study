from collections import deque

node=int(input())
link=int(input())

visited=[0]*(node+1)
maps=[[] for _ in range(node+1)]
print(maps)

for i in range(link):
    a, b= map(int, input().split())
    # maps[a]+=[b] # a에 b 연결
    maps[a].append(b)
    # maps[b]+=[a] # b에 a 연결 -> 양방향
    maps[b].append(a)

print(maps)

#bfs
q=deque()
q.append(1)
visited[1]=1
while q:
    k=q.popleft()
    for i in maps[k]:
        if visited[i]==0:
            q.append(i)
            visited[i]=1
print(sum(visited)-1)
print(visited)


# dfs
def dfs(link):
    visited[link]=1
    for i in maps[link]:
        if visited[i]==0:
            dfs(i)

