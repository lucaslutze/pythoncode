#lucas
#uppgift 1
list1 = ["Lucas", "Akmal", "Martin", "Alfons", "Gabriel"]
list2 = list1.copy()
list2.reverse()

element1 = list2[0]
list1.insert(3,element1)

elementcount1 = list1.count(element1)
print(elementcount1)



#append lägger endast till ett element i slutet av stringen
exempel1 = [1,2,5,3,4]
exempelappend1 = [765,643]
exempel1.append(exempelappend1)


#extend kan läga till flera än 1 element.
exempel2 = [543,6346,234,6547,65]
exempelextend1 = [100, 200]
exempelextend2 = [333,444]
exempel2.extend(exempelextend1)
exempel2.extend(exempelextend2)
print(exempel2)
list1.pop()
#pop tar bort sista elementet
list1.remove("Alfons")
print(list1)
#remove tar bort vad du vill

print(len(list1))


