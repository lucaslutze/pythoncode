
#UPPGIFT 1.1

# ett och a fungerar inte eftersom att de inte har citattecken men annars är dem strings
#4 är en integer
#3.6 är en float
#True är en boolean
#'True' är en string

#UPPGIFT 1.2

#variabel1 är en string
#a är integer
#alpha är boolean
#variabel2 är ingenting

variabel1 = 'a, b, c'
b=12 # b hade inget värde
a = 10
alpha = True
variabel2 = a
variabel3 = 1
variabel4 = b
variablel5 = alpha  #l5 inte 15
print(variabel1)
print(variabel2)
print(variabel3)
print(variabel4)
print(variablel5)

#UPPGIFT 1.3


print(1/3) #print numret 1 delat med 3
print('1/3') #print 1 tredjedel i bråkform
a = 1/3
print(a) #printa a som har ett värde
print('a') #printa bokstaven a

#UPPGIFT 1.4

stefansAge = 15
stefansLength = 170
stefanSkolan = True

lillbabsAge = 80
lillbabsLength = 130
lillbabsSkolan = False

annasAge = 16
annasLength = 150
annasSkolan = True

#UPPGIFT 2.1
#beräknaArea har en variabel som mulitplicerar sida 1 med sida 2
#den använder integer som argument
#svaret blir en integer men det printas inte ut


#alternativtBeräknaArea printar sida 1 gånger sida 2
#den använder integer som argument
#svaret är en integer som printas ut

#adderaSiffror har en variabel som är siffra 1 + siffra 2
#den använder integers som argument
#svaret blir en integer som inte printas ut

#funktion gör samma sak som de innan bara att x och y kan vara annat än integers


#UPPGIFT 2.3



def randomFunktion (x,y):
    xy = (x * y)
    return xy

#UPPGIFT 3

userInput = input(str("skriv något"))
print(userInput+userInput)

#a. Man får strings som läggs ihop

def funktionAnvändbar(x,y):
    summa = x + y
    produkt = summa * 2
    return produkt

#UPPGIFT 3.2

tal1 = float(input("Skriv in tal 1: "))

utförande = input("Välj vad du vill göra med nummret (+,-,*,/,%,//,^,roten: ")

if utförande != "roten":
    tal2 =float(input("Skriv ett till tal"))


if utförande == "+":
    print(tal1 + tal2)
elif utförande == "-":
    print(tal1 - tal2)
elif utförande == "*":
    print(tal1 * tal2)
elif utförande == "/":
    if tal2 == 0:
        print("går ej att dela med noll")
    else:
        print(tal1 / tal2)
elif utförande == "%":
    if tal2 == 0:
        print("går ej att dela med noll")
    else:
        print(tal1 % tal2)
elif utförande == "//":
    if tal2 == 0:
        print("går ej att dela med noll")
    else:
        print(tal1 // tal2)
elif utförande == "^":
    print(num1 ** num2)
elif utförande == "roten":
    print(tal1 ** 0.5)
else:
    print("fungerar inte")


#UPPGIFT