def OddFunction(n):
    ret_list = []
    for i in range(n):
        if (i%2) is 1:
            ret_list.append(i)
    return ret_list


print(OddFunction(8))
