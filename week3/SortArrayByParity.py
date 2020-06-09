#Question
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.

# One Liner
def sortArrayByParity(A):
    return sorted(A, key=lambda x: x % 2)
    return [a for a in A if a%2==0]+[a for a in A if a%2==1]

# Using deque
# def sortArrayByParity(self, A: List[int]) -> List[int]:
#     import collections
#     ans = collections.deque()
#     for i in A:
#         if i % 2 == 0:
#             ans.appendleft(i)
#         else:
#             ans.append(i)
#     return ans

