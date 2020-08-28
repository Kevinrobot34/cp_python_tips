import time
import sys
input = sys.stdin.readline

t = time.time()
n = int(input())
a = [int(input()) for _ in range(n)]
print(time.time() - t)
