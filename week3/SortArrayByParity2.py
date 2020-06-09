# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.\
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# You may return any answer array that satisfies this condition.
#
#
def sortArrayByParityII(A):
    odd = [x for x in A if x % 2]
    even = [x for x in A if not x % 2]
    ans = []
    for i in range(len(even)):
        ans.extend([even[i], odd[i]])
    return ans