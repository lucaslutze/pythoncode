from math import*
from fractions import Fraction

#bråk
num1 = int(input("skriv täjare 1: "))
num2 = int(input("skriv nämnare 1: "))

num3 = int(input("skriv täljare 2: "))
num4 = int(input("skriv nämnare 2: "))

num5 = int(input("skriv täljare 3: "))
num6 = int(input("skriv nämnare 3: "))
#addering av bråk
bråk1 = (num1) / (num2)
bråk2 = (num3) / (num4)
bråk3 = (num5) / (num6)

result2 = Fraction(bråk1 + bråk2 + bråk3)

print(result2)
