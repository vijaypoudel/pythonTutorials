rand_string = "   this is an 2 important string  "

rand_string = rand_string.lstrip()  # remove left spaces
rand_string = rand_string.rstrip()  # remove right spaces

print(rand_string)

print(rand_string.capitalize())
print(rand_string.lower())
print(rand_string.upper())


rand_string_list = ["hello" , "world" , "is" , "beautiful"]

print("".join(rand_string_list))

rand_string_list_2 = rand_string.split()

print("type-" , type(rand_string_list_2))

for i in rand_string_list_2:
    print(type(i))


# alpha numeric checks

letter = "4"
print(letter.isdigit())

