tal1 = float(input("Skriv ett första tal: "))
tal2 = float(input("Skriv ett andra tal: "))
tal3 = float(input("Skriv ett tredje tal: "))

list1 = (tal1, tal2, tal3)
print (list1)



#kollar igenom listan och flyttar minsta talet till vänster
def sort(list1):
    for i in range(len(list1)):
        if list1[i] > list1[i+1]:
            a = list1[i]
            list1[i] = list1[i+1]
            list1[i+1] = a
        print(list1)

sort(list1)


print(list2)
