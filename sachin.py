try:
    sum1 = input("Enter the first number: ")
    sum2 = input("Enter the second number: ")

    add = int(sum1) + int(sum2)
    print(add)
except ValueError:
    print("Please enter valid integers.")
