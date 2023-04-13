#Write a program in Python to reverse a word.

def word_reverse():
    words = input("Please enter your word here: ")
    print(f"The reverse word is {words[::-1]}.")

word_reverse()