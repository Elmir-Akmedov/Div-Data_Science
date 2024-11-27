def max_sum_1(lst):
    lst.remove(sorted(lst)[0])
    return sum(lst)


def max_sum_2(lst):
    removed_num = lst.pop(lst.index(sorted(lst)[0]))
    return sum(lst), removed_num


my_lst = [1, -2, 0, 3, -5, -3, 8]


print(max_sum_1(my_lst))
print(max_sum_2(my_lst))