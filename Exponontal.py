from Binary import binary_search  


def exponential_search(L, key):
    n = len(L)
    if n == 0:
        return -1

    if L[0] == key:
        return 0

    z = 1
    while z < n and L[z] < key:
        z *= 2

    left = z // 2
    right = min(z, n - 1)

    pos = binary_search(L[left:right + 1], key)
    return left + pos if pos != -1 else -1


print(exponential_search(list(range(36)), 3))  
print(exponential_search(list(range(36)), 35))  
print(exponential_search(list(range(36)), 40))  
