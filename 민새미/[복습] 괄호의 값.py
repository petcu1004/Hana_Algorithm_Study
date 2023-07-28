n=list(input())
print(n)

stack=list()
res=0
k=1
for i in range(len(n)):
    if n[i]=='(':
        stack.append(n[i])
        k =2*k
    elif n[i]=='[':
        stack.append(n[i])
        k=3*k
    elif n[i]==')':
        if not stack or stack[-1] =="[":
            res=0
            break
        if stack[i-1]=="(":
            res +=k
        stack.pop()
        k //=2
    else:
        if not stack or stack[-1] =="(":
            res=0
            break
        if n[i-1]=="[":
            res+=k
        stack.pop()
        k//=3

if stack:
    print(0)
else:
    print(res)