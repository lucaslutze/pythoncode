#Lucas Lutze
import random


for i in range(10):
    print(random.randint(30,50))

print()

for i in range(5):
    print(random.uniform(1,10))

print()

for i in range(7):
    print(random.gauss(50,25))

print()

list1 = ("hej", "halloj", "tjena", "tjenixen", "tja")
print(random.sample(list1, k=2))
for i in range(2):
    print(random.choice(list1))

print()

i = 0
while i < 100:
    i += 1
    print(i)
    if i == 50:
        break

print()
#tar in input str och int och försöker printa samtidigt, förebygger med except typeerror.
profession = input("What do you work with? ")
years = int(input("For how many years have you worked with that? "))

try:
    print(profession+years)
except TypeError:
    print("Something went wrong")

print()

#tar in ett nummer från usern och använder try: och except för att förebygga några problem
tal = int(input("Skriv ett nummer"))
try:
    print(tal/0)
except ZeroDivisionError:
    print("Its not possible to divide a number by zero because the denominator multiplied by the result is the numerator")
    print("And anything multiplied by zero is zero so it doesn't work.")

print ()

#öppnar en fil som redan finns, och printar det som finns inuti sedan stänger filen.
file = open('song.txt','r')
print(file.read())
file.close()

#skapar en fil som inte finns och lägger till text sedan stänger filen
path = ("C:\\Users\\LucasLutze\\Desktop\\song2.txt")
file=open(path,'w+')
file.write("bom bam ajdaman")
file.close()