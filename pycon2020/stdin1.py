import time

t = time.time()
n = int(input())
a = [int(input()) for _ in range(n)]
print(time.time() - t)
