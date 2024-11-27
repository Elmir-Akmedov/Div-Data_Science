def sum_of_digits(user_input):
    return sum(int(digit) for digit in str(user_input))


user_input = input("Please enter a number for count digits: ")

print(sum_of_digits(user_input))