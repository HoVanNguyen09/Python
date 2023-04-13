#Write a program to display the first 7 multiples of 7.

def display():

    num = int(input("Please enter your number here: "))

    if num == 8:
        for i in range(1, num):
            i *= 7
            print(i)

display()