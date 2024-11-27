def bubble_sort_1(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def bubble_sort_2(lst):
    for n in range(len(lst)):
        for x in range(1,len(lst)):
            if lst[x-1] > lst[x]:
                lst[x-1], lst[x] = lst[x], lst[x-1]
    return lst
            

my_list = [1, 2, 10, 3, 7, 5, 6, 5, 8, 9, 8, 9, 15, 10]

print(bubble_sort_1(my_list))
print(bubble_sort_2(my_list))