#WAP to separate positive(dương) and negative(âm) numbers from a list.

def pos_neg_list():

    num_list = []

    while True:
        x = input("Nhập số nguyên hoặc nhập 'done' hoặc 'Done' để kết thúc: ")
        if x == 'done' or x == "Done":
            break
        else:
            num_list.append(int(x))

    pos_list = []
    neg_list = []
    for i in num_list:
        if i > 0:
            pos_list.append(i)
        else:
            neg_list.append(i)
    print(pos_list)
    print(neg_list)

pos_neg_list()