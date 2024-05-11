secret_number = 7
while True:
    try:
        number = int(input("Guess the number between 1 to 10"))
        if number == secret_number:
            print("Thank you for guessing the number 7")
            break
    except ValueError:
        print("Please enter a number, you have not entered a number")
print("Thanks for playing the guessing game")