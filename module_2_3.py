my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
number = len (my_list)
index_my_list = 0
while index_my_list < number:
    if my_list [index_my_list] == 0:
        index_my_list = index_my_list + 1
    elif my_list[index_my_list] > 0:
        print(my_list[index_my_list])
        index_my_list = index_my_list + 1
    else:
        break



