from collections import deque
import sys
input=sys.stdin.readline
num = int(input())

for i in range(num):
    n, m = map(int, input().split())
    arr=deque(list(map(int, input().split())))
    cnt = 0
    while arr:
        best = max(arr)
        front = arr.popleft()
        m -= 1
        if best == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            arr.append(front)
            if m < 0 :
                m = len(arr) - 1

