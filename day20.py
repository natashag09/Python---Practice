# Strings (Different Practice)

#Q Function to count spaces in a string
def count_spaces(s):
    c = 0
    for i in s:
        if i == ' ':
            c = c + 1
    return c

print(count_spaces("hello world python"))


#Q Function to remove all spaces from a string
def remove_spaces(s):
    new = ''
    for i in s:
        if i != ' ':
            new = new + i
    return new

print(remove_spaces("hello world"))


#Q Function to count how many times a character appears
def count_char(s, ch):
    c = 0
    for i in s:
        if i == ch:
            c = c + 1
    return c

print(count_char("banana", 'a'))