N = int(input())
H = list(map(int, input().split()))
# dp[i] = min(dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))
dp = [int(1e13)]*N
dp[0] = 0
dp[1] = abs(H[0] - H[1])
for i in range(2, N):
    dp[i] = min(dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))
print(dp[-1])
