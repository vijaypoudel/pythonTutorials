# A-Z - 65-90
# a-z - 97 - 122
# encrypt by shifting the digit by 4, A becomes D
#
#
# def func_name(x,y,z):
#     code here

def add_numbers(num1 , num2):
    return num1+num2

print(add_numbers(5,6))


global_name = "Shilu"

def change_name():
    global global_name
    global_name = "Philu"


change_name()
print(global_name) #name is a global variable

# to access global variable we need to access it through the keyword global


# solve for an equation "x + 4 = 9"

def solve_equation(equation):
    x,add,num1,equal,num2 = str(equation).split()
    num1 , num2 = int(num1) , int(num2)
    return "X = " + str(num2-num1)

print(solve_equation("x + 4 = 9"))





