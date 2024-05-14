import math


multi_list = [ [i]*10 for i in range (1,10)]

for i in range (1,10):
    for j in range(1,10):
        multi_list[i-1][j-1] =  multi_list[i-1][j-1] * j

multi_list = [ [0]*10 for i in range (10)]

for i in range (1,10):
    for j in range(1,10):
        multi_list[i][j] = i*j



for i in range(1,10):
    for j in range(1,10):
        print(multi_list[i][j], end=" || ")
    print()


print(len(multi_list))
print(multi_list[0][0])