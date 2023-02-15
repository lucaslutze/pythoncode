ord = (input("Skriv ett ord: "))

print("Ordet är " + str(len(ord)) + " bokstäver")

print(ord[0:3])

if ord.find("a") != -1:
    print (ord.find("a"))
else :print("Det finns inget a i detta ord.")
if ord.islower():
    print ("Alla är små bokstäver")
else :print ("Alla är inte små bokstäver")
