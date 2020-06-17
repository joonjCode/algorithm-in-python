# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.



from collections import Counter
def relativeSortArray(arr1, arr2):
    c = Counter(arr1)
    ans = []
    ans2 = []
    for n in arr2:
        cnt = c[n]
        ans += [n]*cnt
        del c[n]

    for k, v in c.items():
        ans2 += [k]*v
        
    ans2.sort()

    return ans + ans2

    
test1 = [2,3,1,3,2,4,6,7,9,2,19]
test2 = [2,1,4,3,9,6]

print(relativeSortArray(test1, test2))