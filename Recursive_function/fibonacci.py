def fibonacci (n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        sum = fibonacci(n-1) + fibonacci(n-2)
        return sum



num = int(input("how many fibonacci series to be printed"))

for i in range(num):
    print(fibonacci(i))