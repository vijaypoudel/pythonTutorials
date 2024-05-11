samp_string = "This is a very important String"
print("length : ", len(samp_string))

print(samp_string[0])
print(samp_string[-31])
print(samp_string[0:6])
print(samp_string[4], "there is a space")
print(samp_string[2:])

#alternate character in a string
# slicing excludes the last index in the above it is -1, which is the last character so the last character is out of range.

print(samp_string[0:-1:2])

#reverse a string

print("reverse :" , samp_string[-1:-len(samp_string) -1: -1])

#OR

print("reverse ", samp_string[-1::-1])

#or

print("reverse ", samp_string[::-1])


# concat

print("Hello" + "World")
print("hello" * 3)
num_string = str(4) # typecasting

for char in samp_string:
    print(char)

for i in range(0,len(samp_string) -1 , 2):
    print(samp_string[i] + samp_string[i+1])
