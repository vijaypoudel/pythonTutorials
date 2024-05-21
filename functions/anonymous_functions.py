import random

sum1 = lambda x,y : x+y
print("Sum", sum1(4,5))

can_vote = lambda age:True if age >= 18 else False
print("Can vote ", can_vote(17))

power_list = [
    lambda x:x ** 2,
    lambda x:x ** 3,
    lambda x: x ** 4
]

for func in power_list:
    print(func(4))

attack  = {"quick" : (lambda: "Quick attack"),
           "power" : (lambda: "power attack"),
           "miss" : (lambda: "Ahh miss attack")
           }
print(attack["quick"]()) # run the lambda function !

# i = 10
# while i >= 1:
#     attack_key = random.choice(list(attack.keys()))
#     print(attack[attack_key]())
#     i -= 1

flip_list = []
for i in range(1,101):
    flip_list.append(random.choice(["H","T"]))
print(flip_list.count("H"))
print(flip_list.count("T"))

# map execute a function on each item in a list












