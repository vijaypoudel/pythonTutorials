try:
    a_list = [1,2,3]
    print(a_list[3])
except IndexError:
    print("Sorry that index does not exist")
except:
    print("AN unknown error occurred")


class Dog_name_error(Exception):
    def __init__(self, *args, **kwargs):
            Exception.__init__(self, *args, **kwargs)

try:
    dog_name = input("what is your dog name")
    if any(char.isdigit() for char in dog_name):
        raise Dog_name_error
except Dog_name_error as dg:
    print(dg.args)
    print("Your dogs name can`t contain a number")


num1, num2 = input("Enter 2 values to divide").split()
try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1,num2,quotient))

except ZeroDivisionError:
    print("You cant divide by zero")

else:
    print("you did not raise an exception")

finally:
    print("I execute no matter what")


