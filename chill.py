num1 = int(input("write a number"))
num2 = int(input("write another number"))
num3 = int(input("write a third number"))

if num1<=num2 and num1<=num3:
    print("the smallest one is" +str(num1))
elif num2<=num1 and num2<=num3:
    print("the smallest one is" +str(num2))
else :print("the smallest one is" +str(num3))