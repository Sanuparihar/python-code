first = input ("Enter firsst num:")
operator = input("Enter Operator (+,-,*,/,%) : ")
second = input("enter second num:")

first = int(first)
second = int(second)
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)    
elif operator == "*":
    print(first * second) 
elif operator == "/":
    print(first / second)   
elif operator == "%":
    print(first % second)    
else:
    print("invalid number")            