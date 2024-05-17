class Animal:
    def __init__(self, birth_type="Unknown" ,
                 appearance = "unknown",
                 blooded = "unknown"):
        self._birth_type = birth_type
        self._appearance = appearance
        self._blooded = blooded

    @property
    def birth_type(self):
        return self._birth_type

    @property
    def appearance(self):
        return self._appearance

    @property
    def blooded(self):
        return self._blooded

    @birth_type.setter
    def birth_type(self,birth_type):
        self._birth_type = birth_type

    @appearance.setter
    def appearance(self, appearance):
        self._appearance = appearance

    @blooded.setter
    def blooded(self, blooded):
        self._blooded = blooded


    def __str__(self):
        return "A {} is {} it is {} it is {}".format(
            type(self).__name__ , self.birth_type, self.appearance, self.blooded)