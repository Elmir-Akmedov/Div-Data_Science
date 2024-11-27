def longest_word_length_1(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return len(longest_word)


def longest_word_length_2(sentence):
    return max(len(word) for word in sentence.split())


sentence = "This is a sample sentence"

print(longest_word_length_1(sentence))
print(longest_word_length_2(sentence))
