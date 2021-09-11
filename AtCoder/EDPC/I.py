N = int(input())
p = list(map(float, input().split()))
# dp[i][j] = dp[i-1][j-1] * p[i-1] + dp[i-1][j] * (1 - p[i-1])
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    dp[i+1][0] = dp[i][0] * (1 - p[i])
    for j in range(N):
        dp[i+1][j+1] = dp[i][j] * p[i] + dp[i][j+1] * (1 - p[i])
print(sum(dp[-1][i] for i in range((N+1)//2, N+1)))
