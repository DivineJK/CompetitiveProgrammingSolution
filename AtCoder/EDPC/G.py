import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
outcnt = [0]*N
for i in range(M):
    u, v = map(int, input().split())
    outcnt[u-1] += 1
    graph[u-1].append(v-1)
# dp[i] = max(dp[j] + 1 for j in child[i])
dp = [-1]*N
def f(i):
    if outcnt[i] == 0:
        dp[i] = 0
        return 0
    if dp[i] >= 0:
        return dp[i]
    for j in graph[i]:
        x = f(j)
        if dp[i] < x + 1:
            dp[i] = x + 1
    return dp[i]
for i in range(N):
    dp[i] = f(i)
print(max(dp))
