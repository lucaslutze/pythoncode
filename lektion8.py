
#uppgift 1
ord = input(str("Skriv \"Jensen\": " ))

for letter in ord:
    print("(" + letter + ")")

#uppgift 2
triangel = int(input("skriv ett nummer: "))
for l in range(triangel):
    print("I" + (" "* l) + "\\")


#uppgift 3
j = int(input("Välj ett tal "))

u = "-"

l = " "

print(" " + 2*j*u)

for k in range(0, j):

   print("|" + 2*j*l + "|")

print (" " + 2*j*u)








#uppgift 4
n = int(input("Skriv ett tal: "))
q = 0
for l in range(n):
    l+= 1
    q+= l

print(q)

#uppgift 5
n = int(input("Välj ett tal "))

m = int(input("Välj ett annat tal "))

sum = 0

if n <= m:

   num2 = range(n, m)

   for num1 in num2:

       sum += num1

   print(sum)

else:

   num2 = range(m, n)

   for num1 in num2:

       sum += num1

   print(sum)






secret_word = "alfons gillar benis"
guess = ""
guesses = 0
guessLimit = 3
outOfGuesses = False

while guess != secret_word and not (outOfGuesses):
    if guesses < guessLimit:
        guess = input("Enter guess: ")
        guesses += 1
    else:
        outOfGuesses = True
if outOfGuesses == True:
    print("You lose")
else:
    print("nice")
