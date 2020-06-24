# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        k = min(j-i for i,j in zip(arr,arr[1:]))
        return [[i,j] for i,j in zip(arr,arr[1:]) if j-i ==k]