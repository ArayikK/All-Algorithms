def binary_search(L, key):

    l, r = 0, len(L) - 1

    while l <= r:
        mid = (l + r) // 2

        if L[mid] == key:
            return mid
        elif L[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1

# Քանի որ Exponental.py - ում import եմ արել binary_search - ը, այդ պատճառով այս կտորը գրել եմ,
# որ ստեղի արդյունքները տպվեն միայն այն դեպքում երբ գործարկվում է կոնկրետ այս ֆայլը։

if __name__ == "__main__":
    print(binary_search([1,3, 6, 7, 9, 12, 14], 4))
    print(binary_search([1,3, 6, 7, 9, 12, 14], 12))