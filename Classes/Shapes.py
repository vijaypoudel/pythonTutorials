class Square:
    def __init__(self, height="0",width="0"):
        self.height = height
        self.width = width
    @property
    def height(self):
        print("retrieving the height")
        return self._height

    @property
    def width(self):
        print("retrieving the width")
        return self._width
    @height.setter
    def height(self,value):
        str_value = str(value)
        print("value -----------" , value)
        if str_value.isdigit():
            self._height = value
        else:
            print("Please only enter numbers for height")
    @width.setter
    def width(self, value):
        str_value = str(value)
        if str_value.isdigit():
            self._width = value
        else:
            print("Please only enter numbers for width")

    def get_area(self):
        return int(self.height) * int(self.width)

def main():
    square = Square(100,300)
    # height = input("Enter height: ")
    # width = input("Enter width: ")
    # square.width = width
    # square.height = height

    print("Height :" , square.height)
    print("Width :" , square.width)
    print("Area :" , square.get_area())

main()

