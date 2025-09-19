f=input(" Enter 1 or + to add\n Enter 2 or - to subtract\n Enter 3 or * to multiply\n Enter 4 or / to divide\n:")
if f=="+" or f=="1":
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    c=a+b
    print(c)
elif f=="-" or f=="2":
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    c=a-b
    print(c)
    if b>a:
        print("Since the Second Number ", b, " is greater than the First Number ", a, "\nAnswer is negative.")
elif f=="*" or f=="3":
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    c=a*b
    print(c)
elif f=="/" or f=="4":
    a=int(input("Enter Numerator: "))
    b=int(input("Enter Denominator: "))
    c=a/b
    print(c)
else:
    print("Please select any one of the options Given.")
