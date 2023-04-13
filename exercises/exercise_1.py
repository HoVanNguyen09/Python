#Write a program in Python to display the Factorial of a number.

#Solution 1
def factorial():
    num = int(input("Please enter your number here: "))
    fact = 1
    if num < 0:
        print("Factorial does not exist for negative numbers!")
    elif num == 0:
        print(f"The factorial of {num} is 1!")
    else:
        for i in range(1, num + 1):
            fact *= i
            
        print(f"The factorial of {num} is {fact}!")
        
factorial()

#Solution 2 - Using Recursion
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = int(input("Please enter your number here sesion 2: "))

result = factorial(num)
print(f"The factorial of {num} is {result}")