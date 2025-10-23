def itrrepolation_search(L, key):

    l, r = 0, len(L) - 1
    
    while key <= L[r] and key >= L[l] and l <= r:
        if L[l] == L[r]:
            if L[l] == key:
                return l
            break
            

        pos = l + (key - L[l]) * (r - l) // (L[r] - L[l])

        if L[pos] == key:
            return pos
        elif L[pos] < key:
            l = pos + 1
        else:
            r = pos  - 1
    return -1


print(itrrepolation_search([1, 3, 7, 10, 15, 16,  18, 20, 21, 22, 23, 25, 33, 35, 42, 45, 47, 50, 52], 18))