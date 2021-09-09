s = input()
t = input()
n = len(s)
m = len(t)
# dp[i][j] = max(dp[i-1][j-1]+(s[i]==t[j]), dp[i-1][j], dp[i][j-1])
dp = [[0]*(m+1) for _ in range(n+1)]
sprev = [[-1]*(m+1) for _ in range(n+1)]
tprev = [[-1]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            sprev[i+1][j+1] = i
            tprev[i+1][j+1] = j
        else:
            if dp[i][j+1] > dp[i+1][j]:
                dp[i+1][j+1] = dp[i][j+1]
                sprev[i+1][j+1] = sprev[i][j+1]
                tprev[i+1][j+1] = tprev[i][j+1]
            else:
                dp[i+1][j+1] = dp[i+1][j]
                sprev[i+1][j+1] = sprev[i+1][j]
                tprev[i+1][j+1] = tprev[i+1][j]
l = dp[n][m]
res = [0]*l
u = n
v = m
for i in range(l):
    res[l-i-1] = sprev[u][v]
    u, v = sprev[u][v], tprev[u][v]
for i in range(l):
    print(s[res[i]], end='')
print()
