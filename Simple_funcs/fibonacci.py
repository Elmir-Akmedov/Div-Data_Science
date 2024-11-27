def calc_fibonacci_list_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list
    

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def calc_fibonacci_list_2(n):
    return list(fibonacci_generator(n))


n = int(input("Enter the lenth of the list you want: "))

print(calc_fibonacci_list_1(n))
print(calc_fibonacci_list_2(n))