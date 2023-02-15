import random
num = random.randint(0,20)
print(num)

if (num % 2) == 0:
    print("This random number is even")
else:
    print("This random number is odd")



answer = int(input("What is that number times two? "))

try:
    if answer == (num * 2):
        print("You got it")
    else:
        print("Incorrect")
except TypeError:
    print("Something went wrong, did you enter a number?")

