N, W = map(int, input().split())
# dp[i] = max(sum(v[j] for j s.t. sum(w[j] == i)))
dp = [-1]*(W+1)
dp[0] = 0
for i in range(N):
    w, v = map(int, input().split())
    for j in range(W-w, -1, -1):
        if dp[j] >= 0:
            if dp[j+w] < dp[j] + v:
                dp[j+w] = dp[j] + v
print(max(dp))
