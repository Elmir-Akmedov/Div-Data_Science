def rotate_list(lst, n):
    lst = lst[-n:] + lst[:-n]
    return lst


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(rotate_list(my_list, 2))
