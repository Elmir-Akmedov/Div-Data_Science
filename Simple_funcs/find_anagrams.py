def find_anagrams_1(word, word_list):
    return [w for w in word_list if sorted(w.lower()) == sorted(word.lower())]


def find_anagrams_2(word, word_list):
    anagrams_list = []
    for w in word_list:
        if len(w)!= len(word):
            continue
        for letter in w.lower():
            if letter not in word.lower():
                break
        else:
            anagrams_list.append(w)
    return anagrams_list


word = "listen"
word_list = ["enlist", "google", "inlets", "banana", "inletsada"]


print(find_anagrams_1(word, word_list))
print(find_anagrams_2(word, word_list))

def find_palindromes(word_list):
    return [w for w in word_list if w == w[::-1]]
