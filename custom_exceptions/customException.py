import os

with open("mydata2.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random text \nsecond random text \nthird random text")

try:
    my_file =  open("mydata3.txt", encoding="utf-8")
except FileNotFoundError:
    print("no such file exist in the system")
else:
    print(my_file.read())
finally:
    print("finally")
    my_file.close()
