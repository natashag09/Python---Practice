# Strings (Light Practice)

#Q Take a string and print it in uppercase
s = input('enter string: ')
print(s.upper())


#Q Take a string and check if it starts with a vowel
s = input('enter string: ')

if s[0] == 'a' or s[0] == 'e' or s[0] == 'i' or s[0] == 'o' or s[0] == 'u':
    print('Starts with vowel')
else:
    print('Does not start with vowel')


#Q Take a string and replace all spaces with '_'
s = input('enter string: ')
print(s.replace(' ', '_'))