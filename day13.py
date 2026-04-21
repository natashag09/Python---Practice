# Strings (len, Indexing, Slicing)

#Q Take a string and print its length
s = input('enter string: ')
print(len(s))


#Q Take a string and print first and last character
s = input('enter string: ')
print('first:', s[0])
print('last:', s[-1])


#Q Take a string and print characters from index 1 to 4
s = input('enter string: ')
print(s[1:5])


#Q Take a string and print it in reverse using slicing
s = input('enter string: ')
print(s[::-1])


#Q Take a string and print every second character
s = input('enter string: ')
print(s[::2])


#Q Take a string and check if first and last characters are same
s = input('enter string: ')
if s[0] == s[-1]:
    print('same')
else:
    print('not same')


