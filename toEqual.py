def checkIfSame(a, b):
    if ((a ^ b) != 0):
        print("Numbers are not equal")
    else:
        print("Numbers are equal")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

checkIfSame(a, b)