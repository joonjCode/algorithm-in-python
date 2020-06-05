# No. 2
# Write a function called findGreaterNumbers which accepts an array and returns the number of times a number is followed by a larger number.
# Note that the numbers don't need to be next to each other in the array.
# Any pair where the second number comes later in the array and is also the larger number should count.


def findGreaterNumbers(arr):
    ans = 0
    _arr = [x for c, x in enumerate(arr) for i in arr[c:] if x< i]
    return len(_arr)

print(findGreaterNumbers([1,2,3]))
print(findGreaterNumbers([6,1,2,7]))
print(findGreaterNumbers([5,4,3,2,1]))