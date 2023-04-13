#Write a Python program to count the occurrence of each character in a word.

#Solution 1
from collections import Counter

strings = input("Enter your word here: ")

print("This is the first solution for this exercise!!!")
def counter():
    print(Counter(strings))

counter()

#Solution 2
print("This is the second solution for this exercise!!!")
dicts = {}
def Counters():
    for character in strings:
        if character in dicts:
            dicts[character] += 1
        else:
            dicts[character] = 1
    print (str(dicts))

Counters()