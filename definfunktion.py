tal = int(input("Skriv ett nummer "))
ord = input("Skriv ett ord ")
b = ""
def userInput(ord, tal):
    b = ""
    for c in range(tal):
        b = b + ord
    return b

result = userInput(ord, tal)
print(result)









