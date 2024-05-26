class Alphabet:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        if(self.second >= 100):
            raise StopIteration
        else:
            fib = self.first + self.second
            self.first = self.second
            self.second = fib
            return fib

alpha = Alphabet()

for letter in alpha:
    print(letter)