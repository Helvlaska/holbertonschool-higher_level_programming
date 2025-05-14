def multiply_list_map(my_list=[], number=0):
    list_map = map(lambda x: x * number, my_list)
    return list(list_map)
