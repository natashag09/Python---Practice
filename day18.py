# Functions (Practice)

#Q Create a function to count digits in a number
def count_digits(n):
    c = 0
    while n > 0:
        c = c + 1
        n = n // 10
    return c

print(count_digits(12345))



#Q Create a function to find sum of digits
def sum_digits(n):
    s = 0
    while n > 0:
        d = n % 10
        s = s + d
        n = n // 10
    return s

print(sum_digits(123))


#Q Create a function to check if string is uppercase or lowercase
def check_case(s):
    if s.isupper():
        return "uppercase"
    elif s.islower():
        return "lowercase"
    else:
        return "mixed"

print(check_case("Python"))