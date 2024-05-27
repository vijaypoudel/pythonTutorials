print([2*x for x in range(1,11)])

print(list(filter((lambda x : x%2 != 0), range (1, 11))))

print([x for x in range (1,11) if x % 2 != 0])

print ([x for x in [ i * 2 for i in range (10)] if x % 8 ==0])

# generate 50 random numbers between 1- 1000 which are multiple of 9

import random

print([ x for x in random.sample(range(1,1001),50) if x % 9 ==0])
