#Write a program that appends the type of elements from a list.

#Solution 1
def type_data_list():
    my_list = []
    num = int(input("Enter the number of items: "))
    
    for i in range(num):
        item = input("Please enter item" + str(i+1) + ": ")
        my_list.append(item)

    types_list = []

    for i in my_list:
        if type(i) == int:
            types_list.append("<class 'int'>")
        elif type(i) == float:
            types_list.append("<class 'float'>")
        else:
            types_list.append("<class 'str'>")
    print(types_list)

type_data_list()

#Solution 2
def type_data_list():

    num_list = []

    while True:
        x = input("Nhập số nguyên hoặc nhập 'done' hoặc 'Done' để kết thúc: ")
        if x == 'done' or x == "Done":
            break
        else:
            num_list.append(x)

    type_list = []
    for i in num_list:
        if type(i) == int:
            type_list.append("<class 'int'>")
        elif type(i) == float:
            type_list.append("<class 'float'>")
        else:
            type_list.append("<class 'str'>")
    print(type_list)

type_data_list()