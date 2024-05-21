one_to_10 = range(1,11)

def dbl_num(num):
    return num * 2

print(list(map(dbl_num , one_to_10)))

print(list(map((lambda x: x * 3 ) , one_to_10)))

print(list(map((lambda x, y : x+y), [1,2,3], [3,4,5])))

import random

list_of_hundred = list(random.sample(range(1,1001),100))
print(list(filter((lambda x : x % 9 == 0), list_of_hundred)))


