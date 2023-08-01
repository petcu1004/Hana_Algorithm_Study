s=int(input())

display=1 #화면에 보여지는 이모티콘 수
cnt=0 #총 연산 시간
clip= 0 #클립보드에 있는 이모티콘 수

clip=display

display=clip

display-=1

def check(n):
    if n==1:
        clip=display
    elif n==2:
        display=clip
    elif n==3:
        display-=1


def dfs(n):
    if display==s:
        return cnt
    # for i in range(3):



