import numpy as np
import matplotlib.pyplot as plt
import time

already_sorted = False
reps = 5
first_n, last_n, step_n = 10000, 500000, 10000
times, sizes = [], []
for n in range(first_n, last_n, step_n):
    sum_time = 0
    for r in range(reps):
        if already_sorted:
            L = list(np.arange(n)) # Generates list [0,1,2,...,n-1]
        else:    
            L = list(np.random.randint(1000000, size=n)) # Generates list with n random integers
        start = time.time()
        L.sort()
        elapsed_time = time.time() - start
        sum_time += elapsed_time
    times.append(sum_time/reps) # Display average time per repetition
    sizes.append(n)
    print('List length: {:3}, running time: {:7.5f} seconds'.format(sizes[-1],times[-1]))
    
    
#plt.close('all')  # Uncomment to close all previous figures prior to drawing a new one
fig, ax = plt.subplots()
plt.plot(sizes,times)
ax.set_xlabel('n')
ax.set_ylabel('running time (seconds)')
fig.suptitle('Running time for default sorting algorithm', fontsize=16)


