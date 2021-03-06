import sys
read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
arr = [i for i in range(1, N+1)]
isvisited = [False] * (N)
ans = []


def dfs(depth):
    # 기저 조건
    if depth == M:
        print(*ans)
        return

    # 반복 조건
    for i in range(N):
        ans.append(arr[i])
        dfs(depth+1)
        ans.pop()


dfs(0)
