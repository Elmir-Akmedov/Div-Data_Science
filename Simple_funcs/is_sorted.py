def is_sorted_1(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def is_sorted_2(arr):
    return arr == sorted(arr)


def is_sorted_3(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

array = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

print(is_sorted_1(array))
print(is_sorted_2(array))
print(is_sorted_3(array))