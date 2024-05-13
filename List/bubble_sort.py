## bubble sort
## cycle through the entire list
### the end goal is to have the largest number sorted out



import random
list_start = []

for i in range(5):
    list_start.append(random.randrange(1,9))

for i in list_start:
     print(i)

### Sorting starts

len_list = len(list_start)
sorted_list = list_start

for i in range(len_list -1,0,-1):
    print("i:",i)
    for j in range(0,i):
        max = sorted_list[j]
        if sorted_list[j] >= sorted_list [j+1]:
            sorted_list[j] = sorted_list [j+1]
            sorted_list[j+1] = max
for i in sorted_list:
     print(i)




