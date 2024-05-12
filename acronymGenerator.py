rand_string = input("Please generated the name of your favorite IPL team in full")
split_rand_string = rand_string.split()
acronym = ""
for i in split_rand_string:
    for j in i:
        acronym += j
        break
print("Here is your acronym - ", acronym.upper())

# another way
for i in split_rand_string:
    print(i[0], end="")