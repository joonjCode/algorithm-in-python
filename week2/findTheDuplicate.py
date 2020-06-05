# No. 1
# Write a function called findTheDuplicate which accepts an array of numbers containing a single duplicate.
# The function returns the number which is a duplicate or undefined if there are no duplicates.

from collections import Counter;

def findTheDuplicate(arr):
    _arr = Counter(arr)
    ans = 0
    # print(_arr)
    for i in _arr.elements():
        if _arr[i] == 2:
            return i
print(findTheDuplicate([6,1,9,5,3,4,9]))
print(findTheDuplicate([2,1,3,4]))
# findTheDuplicate([1,2,1,4,3,12])
