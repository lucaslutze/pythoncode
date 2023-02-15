import random
#uppgift 1
x = 0
while x < 22:
    if x % 2 == 0:
        print(x)
    x += 1
print("klart")

#uppgift 2
tak = 101
summa = 0
while summa <= 101:
    n = int(input("skriv ett tal: "))
    summa += n
    print("summa är " + str(summa))
print("over 100")

#uppgift 3
spel =  str(input("vill du spela?"))
while spel == "ja":
    spel = input("vill du spela igen?")
else: print("jag vill inte spela med dig heller")

#uppgift 4
guessLimit = 10
outOfGuesses = False
a = random.randint(0,100)
svar = int(input("gissa nummret"))
guesses = 1

while svar != a and not (outOfGuesses):

    if svar > a:
        svar = int(input("lower: "))
    elif svar < a:
        svar = int(input("higher: "))
    else:
        print("u got it")
    guesses += 1
    if guesses >= guessLimit:
        outOfGuesses = True
print("du suger")