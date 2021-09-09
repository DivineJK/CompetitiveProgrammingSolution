N, W = map(int, input().split())
V = 1000*N
# dp[i] = min(sum(w[j] for j s.t. sum(v[j] == i)))
dp = [int(1e13)]*(V+1)
dp[0] = 0
for i in range(N):
    w, v = map(int, input().split())
    for j in range(V-v, -1, -1):
        if dp[j+v] > dp[j] + w:
            dp[j+v] = dp[j] + w
t = V
while dp[t] > W:
    t -= 1
print(t)
