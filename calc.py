x=(input("Enter any number: "))
y=(input("Enter another number: "))
z=input("Enter any operator(+,-,/,*): ")
if x=="":
    print("Type number in 1st column.")
    if y=="":
        print("Type number in 2nd column also.")
        if z=="":
            print("Type operator also.")
    elif z=="":
        print("Type operator also.")
elif y=="":
    print("Type number in 2nd column.")
    if z=="":
        print("Type operator also.")
else:
    x=float(x)
    y=float(y)
    if z=="+":
        print("You have selected Addition operator. Your answer is: "+str(x+y))
    elif z=="-":
        print("You have selected Subtraction operator. Your answer is: "+str(x-y))
    elif z=="/":
        print("You have selected Division operator. Your answer is: "+str(x/y))
    elif z=="*":
        print("You have selected Multiplication operator. Your answer is: "+str(x*y))
    else:
        print("Either operator is not typed or wrong operator is typed.")
