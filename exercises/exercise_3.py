#Write a Python program to reverse a number.

#Solution 1
def reversed_number():
    reversed_num = 0
    num = int(input("Please enter your number here: "))
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print(reversed_num)

reversed_number()

#Solution 2
def reversed_number():
    num = input("Please enter your number here: ")
    print(int(num[::-1]))

reversed_number()