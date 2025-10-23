def linear_search(L, key):
    for i in range(len(L)):
        if L[i] == key:
            return i
    return "No matches found"


print(linear_search([2, 6, 1, 9, 7], 0))
