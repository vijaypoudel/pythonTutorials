def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def chnage_list(list, func):
    odd_list =[]
    for i in list:
        if func(i):
            odd_list.append(i)
    return odd_list

a_list = range(1,10)
print(chnage_list(a_list,is_it_odd))

