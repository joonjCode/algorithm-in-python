# 2. merge two sorted arrays
# Write a function that accepts two sorted arrays of numbers
# return a combined array of the numbers in sorted order
# The optimal solution is O(n) linear time, if you get stuck you can research ‘merge sort’
# input: [3, 4, 7, 8] [1, 5, 6, 9]
# output: [1, 3, 4, 5, 6, 7, 8, 9]

def mergeArrays(arr1, arr2):
    ans = []
    i = j = 0
    print(i, j)
    while len(arr1) > i and len(arr2) > j:
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    while i < len(arr1):
        ans.append(arr1[i])
        i += i
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    return ans


arr1 = [3, 4, 7, 8]
arr2 = [1, 5, 6, 9]
print(mergeArrays(arr1, arr2))
