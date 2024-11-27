def count_vowels(user_input):
    return sum(1 for char in user_input.lower() if char in vowels)

user_input = input("Please enter a word: ")
vowels = ["a", "e", "i", "o", "u"]


print(count_vowels(user_input))
