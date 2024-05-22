# iterable vs iterators
# iterable - object with iter method
#iterator -  object is with next method

samp_str = iter("Sample")

print("Char :", next(samp_str))
print("Char :", next(samp_str))
print("Char :", next(samp_str))
print("Char :", next(samp_str))
print("Char :", next(samp_str))

