def is_sorted(L):
    for i in range(1, len(L)):
        if L[i] < L[i - 1]:
            return False
    return True

def partition(A, l, r):
    pivot = A[r]
    i = l - 1
    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(L, l=0, r=None):
    if is_sorted(L):
        return L
    if r is None:
        r = len(L) - 1
    if l < r:
        p = partition(L, l, r)
        quick_sort(L, l, p - 1)
        quick_sort(L, p + 1, r)
    return L


print(quick_sort([1, 4, 3, 2, 7, 6, 3]))
print(quick_sort([1]))
print(quick_sort([]))