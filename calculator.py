num1=float(input("enter num1:",))
num2=float(input("enter num2:",))
operator=input("enter operator: ")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    if(num2==0):
        print("indefinite")
    else:
        print(num1/num2)
elif operator=="**":
    print("num2",num1**num2)
else:
    print("invalid operator")