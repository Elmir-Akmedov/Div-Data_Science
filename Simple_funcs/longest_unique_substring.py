def longest_unique_substring_1(word):
    substr_start = 0
    substr_end = 0
    
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            if len(set(word[i:j])) == len(word[i:j]):
                if j - i > substr_end - substr_start:
                    substr_start = i
                    substr_end = j
    return len(word[substr_start:substr_end])

[]
def longest_unique_substring_2(word):
    
    start = 0
    max_length = 0
    substring = set()

    for end in range(len(word)):
        while word[end] in substring:
            substring.remove(word[start])
            start += 1
        substring.add(word[end])
        max_length = max(max_length, end - start + 1)
    return max_length


word = "abcabcbbabcdpdppacysgsrdaaabcbb"

print(longest_unique_substring_1(word))
print(longest_unique_substring_2(word))