def count_frequency_1(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


def count_frequency_2(lst):
    return {item: lst.count(item) for item in set(lst)}


def count_frequency_3(lst):
    frequency = []
    for item in lst:
        frequency.append((item, lst.count(item)))
    return frequency


my_list = [1, 2, 3, 2, 3, 4, 5, 6, 2, 3]


print(count_frequency_1(my_list))
print(count_frequency_2(my_list))
print(count_frequency_3(my_list))