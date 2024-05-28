def is_prime(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
        return True

def gen_prime(max_number):
    for num1 in range(2, max_number):
        if is_prime(num1):
            yield num1


print(type(gen_prime(50)))

for i in gen_prime(50):
    print(i)

prime = gen_prime(50)

print(next(prime))

print("===-=-=-=-=-=-=-=-=-")

double = (x * 2 for x in range(10))
print(next(double))
print(next(double))
print(next(double))
print(next(double))





