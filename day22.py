# Lists (Intermediate)

#Q Remove duplicates from list
def remove_duplicates(L):
    new = []
    for i in L:
        if i not in new:
            new.append(i)
    return new

print(remove_duplicates([1,2,2,3,4,4,5]))


#Q Count frequency of an element
def frequency(L, x):
    c = 0
    for i in L:
        if i == x:
            c = c + 1
    return c

print(frequency([1,2,2,3,2,4], 2))


#Q Merge two lists
def merge(L1, L2):
    return L1 + L2

print(merge([1,2], [3,4]))








