#Write a program to print n natural numbers in descending order using a while loop.

def descended_number():

    num = int(input("Please enter your natural number here: "))

    while num > 0:
        print(num)
        num -= 1

descended_number()

#Write a program to print n natural numbers in descending order using a for loop.
def descended_number():

    num = int(input("Please enter your natural number here: "))
    
    for i in range(num, 0, -1):
        print(i)

descended_number()