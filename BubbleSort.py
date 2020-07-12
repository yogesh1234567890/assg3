mylist = [12, 5, 11, 9, 3, 7, 10, 4, 1]
newlist = sorted(mylist)
num = int(input("Enter any num to search: "))
print(len(newlist))
pos = -1
def binarysearch(newlist, n):
    lower = 0
    upper = len(newlist) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        if newlist[mid] == n:
            globals()['pos'] = mid
            return True

        else:
            if newlist[mid] < n:
                lower = mid + 1

            else:
                upper = mid - 1

    return False


if binarysearch(newlist, num):
    print("found at ", pos + 1)

else:
    print("Not Found")


