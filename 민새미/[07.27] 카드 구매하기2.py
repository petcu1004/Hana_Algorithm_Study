n=int(input())
cards=[0]
cards+=list(map(int, input().split()))

print(cards)

# def dp(n):
#     arr=[0]*(n+1)

#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             arr[i]=min(cards[i], arr[i-j]+cards[j])

#     print(arr)
#     return arr[n]

# print(dp(n))