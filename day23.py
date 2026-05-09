# Lists (Intermediate)

#Q Remove duplicate elements from a list
def remove_duplicates(L):
    new = []
    for i in L:
        if i not in new:
            new.append(i)
    return new

print(remove_duplicates([1,2,2,3,4,4,5]))


#Q Count frequency of an element in list
def frequency(L, x):
    c = 0
    for i in L:
        if i == x:
            c = c + 1
    return c

print(frequency([1,2,2,3,2,4], 2))


#Q Find common elements between two lists
def common(L1, L2):
    new = []
    for i in L1:
        if i in L2 and i not in new:
            new.append(i)
    return new

print(common([1,2,3,4], [3,4,5,6]))