N = int(input())
# dp[i][j] = max(dp[(i+1)%3][j-1], dp[(i+2)%3][j-1]) + x[i][j]
dp = [[0]*(N+1), [0]*(N+1), [0]*(N+1)]
for i in range(1, N+1):
    a, b, c = map(int, input().split())
    dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + a
    dp[1][i] = max(dp[2][i-1], dp[0][i-1]) + b
    dp[2][i] = max(dp[0][i-1], dp[1][i-1]) + c
print(max(dp[0][N], dp[1][N], dp[2][N]))
