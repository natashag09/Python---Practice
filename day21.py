# Strings + Lists (Light)

#Q Convert string into list of characters
def to_list(s):
    L = []
    for i in s:
        L.append(i)
    return L

print(to_list("python"))


#Q Count words in a string
def count_words(s):
    words = s.split()
    return len(words)

print(count_words("I am learning python"))


#Q Find longest word in a sentence
def longest_word(s):
    words = s.split()
    long = words[0]
    for i in words:
        if len(i) > len(long):
            long = i
    return long

print(longest_word("I love learning python programming"))