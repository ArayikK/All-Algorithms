import math


def jump_search(L, key):

    step = round(math.sqrt(len(L)))
    pos = 0

    while pos < len(L) and L[pos] < key:
        pos += step

    for i in range(max(0, pos - step), min(len(L), pos + 1)):
        if L[i] == key:
            return i
    return "No such element"

print(jump_search([1,3,5,7,13,17,22,26,34,37,45,78,90], 100))