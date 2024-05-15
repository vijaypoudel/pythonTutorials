import os

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random text \nsecond random text \nthird random text")

with open("mydata.txt", encoding = "utf-8") as my_file:
    print(my_file.read())


