# Lists + Functions (light)

#Q Function to find sum of list
def sum_list(L):
    s = 0
    for i in L:
        s = s + i
    return s

print(sum_list([1, 2, 3]))


#Q Function to find maximum in list
def max_list(L):
    m = L[0]
    for i in L:
        if i > m:
            m = i
    return m

print(max_list([10, 5, 20]))


#Q Function to reverse a list
def reverse_list(L):
    return L[::-1]

print(reverse_list([1, 2, 3]))