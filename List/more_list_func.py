import random

num_list = []
for i in range(5):
    num_list.append(random.randrange(1,9))

num_list.sort()
num_list.reverse()
num_list.insert(2,5)

# delete first occurance of a value
num_list.remove(10)
num_list.pop(2)

