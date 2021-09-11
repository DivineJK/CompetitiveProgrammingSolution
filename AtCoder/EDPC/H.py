H, W = map(int, input().split())
mod = int(1e9) + 7
# dp[i][j] = (S[i][j] == '#' ? 0 : dp[i-1][j] + dp[i][j-1])
dp = [[0]*(W+2) for _ in range(H+2)]
S = ["#"*(W+2)]+['#'+input()+'#' for _ in range(H)]+["#"*(W+2)]
dp[1][0] = 1
for i in range(H):
    for j in range(W):
        if S[i+1][j+1] == '.':
            dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j]) % mod
print(dp[H][W])
