def multi_return(num1,num2):
    return (num1*num2) , (num1/num2)

multi , devis = multi_return(10,5)
print(multi,devis)

## Prime number detection

def is_prime(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
    return True

while True:
    try:
        number = int(input("Input the number you want to check if it is prime or not  "))
        if is_prime(number):
            print("The number is a prime")
        else:
            print("The number is not a prime")
        break
    except ValueError:
        print("please enter a number")
        continue

## unknown number of args

def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print("Sum :" , sum_all(1,2,34,5,6,7,765,7547,456,54,64,643,645,645))