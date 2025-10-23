def bubble_sort(L):
    n = len(L)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (L[j] > L[j + 1]):
                L[j], L[j + 1] = L[j + 1], L[j]
    return L

print(bubble_sort([1, 4, 2, -7, -3]))
print(bubble_sort([1, -7]))
print(bubble_sort([-3]))
print(bubble_sort([]))



            