import time

start = time.time()

benchmark_float = 0.0

for i in range(10**10):
    benchmark_float += 1.0
for i in range(5*(10**9)):
    benchmark_float *= 1.0
for i in range(2*(10**9)):
    benchmark_float /= 1.0

end = time.time()
time_taken = end - start
print(f"Float operation benchmark took {time_taken} seconds")