import time

start = time.time()

benchmark_var = 0

for i in range(10**10):
    benchmark_var += 1
for i in range(5*(10**9)):
    benchmark_var *= 1
for i in range(2*(10**9)):
    benchmark_var /= 1
