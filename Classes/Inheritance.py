class Animal:
    def __init__(self, birth_type="Unknown" ,
                 appearance = "unknown",
                 blooded = "unknown"):
        self._birth_type = birth_type
        self._appearance = appearance
        self._blooded = blooded

    @property
    def birth_type(self):
        print("read", self.__class__)
        return self._birth_type

    @property
    def appearance(self):
        return self._appearance

    @property
    def blooded(self):
        return self._blooded

    @birth_type.setter
    def birth_type(self,birth_type):
        print("write", self.__class__)
        self._birth_type = birth_type

    @appearance.setter
    def appearance(self, appearance):
        self._appearance = appearance

    @blooded.setter
    def blooded(self, blooded):
        self._blooded = blooded


    def __str__(self):
        print("hello there", self.__class__)
        return "A {} is {} it is {} it is {}".format(
            type(self).__name__ , self.birth_type, self.appearance, self.blooded)

class Mammal(Animal):
    def __init__(self , birth_type="born_alive", apperance = "hair or fur",
                 blooded="warm blooded",
                 nurse_young = False):
        Animal.__init__(self,birth_type,apperance,blooded)
        self._nurse_young = nurse_young

    @property
    def nurse_young(self):
        return self._nurse_young

    @nurse_young.setter
    def nurse_young(self, nurse_young):
        print("hello there")
        self._nurse_young = nurse_young

    def __str__(self):
        return super().__str__() + "and it is {} they nurse young".format(self.nurse_young)


class Reptile(Animal):
    def __init__(self , birth_type="born in an egg", apperance = "dry scales",
                 blooded="cold blooded"):
        Animal.__init__(self,birth_type,apperance,blooded)

def main():

    animal2 = Mammal("born alive", "hair or fur", "warm blooded" , True)

    animal2.nurse_young = False
    print(animal2)

    # animal3 = Reptile("born in an egg",
    #                   "dry scales".lower(),
    #                   "cold bloooooded")
    #
    # print(animal3)

main()