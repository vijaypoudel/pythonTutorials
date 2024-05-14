import math

even_list = [i*2 for i in range(10)]

for k in even_list:
    print(k,end=",")

num_list = [1,2,3,4,5]
list_of_values = [[math.pow(m,2), math.pow(m,3), math.pow(m,4) ] for m in num_list]

for k in list_of_values:
    print(k)

print([0]*10)
multi_d_list = [[0]*10 for i in range(10)]



for i in range (10):
    for j in range(10):
        print(multi_d_list[i][j], end=" || ")
    print()