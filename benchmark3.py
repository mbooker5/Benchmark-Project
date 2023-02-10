import time

start = time.time()

required_length = (5 * (10 ** 9))
array = [0] * required_length

for ind,num in enumerate(array):
    # read array items
    zero = num

    #write array items
    array[ind] = ind

end = time.time()

time_taken = end - start
print(f"Memory benchmark took {time_taken} seconds")

    

