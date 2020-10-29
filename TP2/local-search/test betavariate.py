# import the required libraries 
import random 
import numpy
import math
import matplotlib.pyplot as plt 


# store the random numbers in a 
# list 
nums = [] 
nums2 = []
bars = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
low = 10
high = 100
mode = 20

for i in range(100): 
    temp = random.betavariate(1, 0.2) 
    nums.append(temp) 
    i = 0
    while(temp>0):
        temp -= 0.025
        i += 1
    bars[i-1] += 1
nums.sort()	

for i in range (1000):
    test = numpy.random.exponential(1)
    print(round(test) + 1, round(math.exp(-test), 2))
    nums2.append(test)
nums2.sort()

# print(nums[0])
# # plotting a graph
plt.plot(nums2) 
# #plt.plot(bars) 
# plt.show()
