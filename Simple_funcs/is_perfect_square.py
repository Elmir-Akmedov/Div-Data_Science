def is_perfect_square(num):
    return num**0.5 == int(num**0.5)

user_num = int(input('Please enter a number: '))

if is_perfect_square(user_num):
    print(f'{user_num} is a perfect square')
else:
    print(f'{user_num} is not a perfect square')