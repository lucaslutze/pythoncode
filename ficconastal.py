first = int(input("Förtsa talet i summan "))
last = int(input("Sista talet i summan "))
const = int(input("Välj ett tal, vne fan "))
def sigma(first, last, const):
    sum = 0
    for i in range(first, last + 1):
        sum += const * i
    return sum
sigma()
