#Write a program that appends the square of each number to a new list.

def new_list():

    num_list = []

    while True:
        x = input("Nhập số nguyên hoặc nhập 'done' để kết thúc: ")
        if x == 'done' or x == "Done":
            break
        else:
            num_list.append(int(x))

    squares_list = []
    for i in num_list:
        squares_list.append(i ** 2)
    
    print(squares_list)

new_list()