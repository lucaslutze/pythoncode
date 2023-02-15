# lucas
# Uppgift 1 N.1

import math

num1 = int(input("Skriv ett tal "))
num2 = int(input("skriv ett annat tal "))
print("kvoten blev " + str(num1 / num2) + "!")
print("resten blev " + str(num1 % num2))
print(str(num1), "/", str(num2), "=", str(math.floor(num1 / num2)), "och", str(num1 % num2), "i rest")

# Uppgift 2 N.1 och N.2

sif1 = int(input("Skriv ett heltal "))
sif2 = float(input("Skriv ett decimaltal "))
print("float av heltalet blev ", float(sif1))
print("int av decimaltalet blev", int(sif2))

# Det vi ser är att integern blir till float men eftersom den inte har några decimaler så blir det ingen skiullnad.
# När man gör om floaten till en integer så kapas alla decimalerna bort.

# Uppgift 2 N.3

x = 2.5
print("x = 2.5")
print(math.ceil(x))
print(math.floor(x))

# När man använder sig av ceil så avrundas talet uppåt oavsätt vad decimalerna är.
# När man använder sig av floor så avrundas talet neråt oavsätt vad decimalerna är.

# Uppgift 2 N.4

a = float(input("Välj ett decimaltal "))
b = int(a)
print("Det minsta man kan dela ditt tal med är ")
print((math.gcd(b)))

# Uppgift 2 N.5

import decimal

print("Omkretsen för en cirkel med radien 10 är ")
radie = 10
omkrets = (10 * math.pi * 2)
o1 = decimal.Decimal(omkrets)
print(o1)

# Uppgift 3

a = int(input("Skriv det första talet "))
b = int(input("Skriv det andra talet "))
c = int(input("Skriv det tredje talet "))
d = int(input("Skriv det fjärde talet "))

if a <= b and a >= c and a >= d: print(str(a), "är det näst största talet")
if a >= b and a <= c and a >= d: print(str(a), "är det näst största talet")
if a >= b and a >= c and a <= d: print(str(a), "är det näst största talet")
if b <= a and b >= c and b >= d: print(str(b), "är det näst största talet")
if b >= a and b <= c and b >= d: print(str(b), "är det näst största talet")
if b >= a and b >= c and b <= d: print(str(b), "är det näst största talet")
if c <= a and c >= b and c >= d: print(str(c), "är det näst största talet")
if c >= a and c <= b and c >= d: print(str(c), "är det näst största talet")
if c >= a and c >= b and c <= d: print(str(c), "är det näst största talet")
if d <= a and d >= b and d >= c: print(str(c), "är det näst största talet")
if d >= a and d <= b and d >= c: print(str(c), "är det näst största talet")
if d >= a and d >= b and d <= c: print(str(c), "är det näst största talet")

lista = [a, b, c, d]
lista.sort()
print(str(lista[2]), "är det näst största talet")


