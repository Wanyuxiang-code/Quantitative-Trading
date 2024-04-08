
import statistics
import random
import numpy as np
import math

l = [-1, 1]
sample1 = random.choices(l, k=1000)
print("Standard Deviation of the sample 1 is % s "
					%(statistics.stdev(sample1)))

sample2 = np.zeros(1000)
sample2[0] = 1000
print("Standard Deviation of the sample 2 is % s "
					%(statistics.stdev(sample2)))

print("square root of 1000 is % s" %(math.sqrt(1000)))