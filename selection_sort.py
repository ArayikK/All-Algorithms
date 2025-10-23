def selection_sort(L):
    n = len(L)
    for i in range(n):
        min_ind = i

        for j in range(i + 1, n):
            if (L[j] < L[min_ind]):
                min_ind = j
        L[i], L[min_ind] = L[min_ind], L[i]
    return L

print(selection_sort([1, 4, 2, -7, -3]))
print(selection_sort([1, -7]))
print(selection_sort([-3]))
print(selection_sort([]))