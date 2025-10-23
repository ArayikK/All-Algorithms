def is_sorted(L):
    for i in range(1, len(L)):
        if L[i] < L[i - 1]:
            return False
    return True
def merge(a_l, a_r):

    a = []

 

    while a_l and a_r:
        if a_l[0] < a_r[0]:
            a.append(a_l.pop(0))

        else:
            a.append(a_r.pop(0))

    if a_l:
        a += a_l
    if a_r:
        a += a_r

    return a


def merge_sort(L):
    if is_sorted(L):
        return L
    if len(L) == 1:
        return L
    mid = len(L) // 2


    left = L[:mid]
    right = L[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


print(merge_sort([1,3,2,4,3,9,8,6,0,7,4]))
print(merge_sort([1]))
print(merge_sort([]))
            