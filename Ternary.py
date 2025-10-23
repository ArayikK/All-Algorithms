def ternary(L, key):

    l, r = 0, len(L) - 1

    while l < r:
        mid1, mid2 = (r + l) // 3,  2 * (r + l) // 3

        if L[mid1] == key:
            return mid1
        
        if L[mid2] == key:
            return mid2
        
        if L[mid1] > key:
            r = mid1

        elif L[mid2] < key:
            l = mid2

        else:
            l = mid1
            r = mid2
        
    return "No such element"


print(ternary([1,4,7,9,12,34,56], 0))
print(ternary([1,4,7,9,12,34,56], 4))
print(ternary([1,4,7,9,12,34,56], 56))