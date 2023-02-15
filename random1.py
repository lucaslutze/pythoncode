#Lucas Lutze
#TEI22A

import random

print("----------------------------")

#Random ints
for i in range(10):
    print(random.randint(30,50))

print("----------------------------")

#Random floats
for i in range(5):
    print(random.uniform(1,10))

print("----------------------------")

#Random gaussians
for i in range(7):
    print(random.gauss(50,25))

print("----------------------------")

#Break
i = 0
while i < 100:
    i += 1
    print(i)
    if i == 50:
        break

print("----------------------------")

#Exceptions
profession = input("What do you work with? ")
years = int(input("For how many years have you worked with that? "))

try:
    print(profession+years)
except TypeError:
    print("Something went wrong")

print("----------------------------")

#Exceptions 2
tal = int(input("Skriv ett nummer"))
try:
    print(tal/0)
except ZeroDivisionError:
    print("Its not possible to divide a number by zero because the denominator multiplied by the result is the numerator")
    print("And anything multiplied by zero is zero so it doesn't work.")

print("----------------------------")


