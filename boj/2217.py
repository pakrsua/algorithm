# 2217 로프
import sys

N = int(sys.stdin.readline())
arr = []
ans = 0
for t in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for i in range(N):
    weight = arr[i] * (N-i)
    if weight > ans:
        ans = weight
print(ans)