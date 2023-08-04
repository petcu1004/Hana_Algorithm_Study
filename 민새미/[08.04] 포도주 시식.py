n = int(input())
# arr = list()
# for i in range(n):
#     arr.append(int(input()))

arr = [int(input()) for _ in range(n)]

dp = []

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
else:
    dp.append(arr[0])
    dp.append(arr[0] + arr[1])
    dp.append(max(arr[0] + arr[2], arr[1] + arr[2], dp[1]))
    for i in range(3, n):
        # 2칸 + 띄고 1칸 / 1칸 + 다음+다음 / 안가고 바로 이전
        dp.append(max(dp[i - 2] + arr[i], dp[i - 3] + arr[i] + arr[i - 1], dp[i - 1]))

print(dp[-1])
