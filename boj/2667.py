# 2667 단지번호붙이기
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def dfs(i,j):
    global ans, hap
    visited[i][j] = 1
    for d in range(4):
        nr = i +dr[d]
        nc = j +dc[d]
        if nr >= 0 and nr < N and nc >= 0 and nc < N:
            if arr[nr][nc] == '1' and visited[nr][nc] == 0:
                hap += 1
                dfs(nr,nc)
    return

N = int(input())
arr = []
visited = [[0] * N for _ in range(N)]
ans = 0
ans_arr = []
for n in range(N):
    arr.append(list(input()))

for i in range(N):
    for j in range(N):
        hap = 0
        if arr[i][j] == '1' and visited[i][j] == 0:
            dfs(i,j)
            ans += 1
            ans_arr.append(hap)
print(ans)
ans_arr.sort()
for i in ans_arr:
    print(i+1)