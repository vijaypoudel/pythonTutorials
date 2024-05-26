print([2*x for x in range(1,11)])

print(list(filter((lambda x : x%2 != 0), range (1, 11))))

print([x for x in range (1,11) if x % 2 != 0])