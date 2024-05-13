import math

def rectangle_area():
    length = float(input("Enter the length"))
    width = float(input("Enter the width"))
    print("The area of the rectangle is " , length * width)

def circle_area():
    radius = float(input("Please enter the radius of the circle"))
    area = math.pi * math.pow(radius,2)
    print("The are of the circle is ", area)

def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")
        
def main():
    shape = input("Please enter whose area you want to calculate - rectangle or circle")
    get_area(shape)

main()

