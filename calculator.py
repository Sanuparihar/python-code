num1 = float (input("Entr the number="))
num2 = float(input("Enter another number="))
choice = input("Enter the operation + , - ,*  , / ")
if choice == "+":
    sum = num1+num2
    print ("the sum is",sum)
elif choice == "-":
    diff = num1 - num2
    print("the diff is", diff)
elif choice == "*":
    mul= num1*num2
    print("the multiple", mul)
elif choice == "/":
    div= num1 /num2
    print ("the divide" , div)
else:
    print("Invalid choice")

  