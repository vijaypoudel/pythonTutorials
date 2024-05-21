from functools import reduce

print(reduce((lambda x,y : x+y), range(1,6)))
print(list(map((lambda x,y : x+ y), range(1,6), range(1,6))))