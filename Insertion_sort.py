def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]

        j = i - 1
        while j >= 0:
            if arr[j] > tmp:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = tmp
    return arr


print(insertion_sort([1,7,5,3,9,7,4,3]))
print(insertion_sort([1,3]))
print(insertion_sort([0]))
print(insertion_sort([]))
print(insertion_sort([1,1,1,1,2,1,1,1]))
