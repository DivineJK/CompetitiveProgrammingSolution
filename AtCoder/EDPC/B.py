N, K = map(int, input().split())
H = list(map(int, input().split()))
# dp[i] = min(dp[i-j]+abs(H[i]-H[i-j]) for j in range(1, K+1))
dp = [int(1e13)]*N
dp[0] = 0
for i in range(1, N):
    t = K
    if i < K:
        t = i
    for j in range(t):
        if dp[i] > dp[i-j-1] + abs(H[i]-H[i-j-1]):
            dp[i] = dp[i-j-1] + abs(H[i]-H[i-j-1])
print(dp[-1])
