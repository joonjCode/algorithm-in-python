# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

from collections import OrderedDict, Counter


def firstUniqChar(s):
    for i,j in OrderedDict(Counter(s)).items():
        if j == 1:
            return s.index(i)
    return -1



test = 'leetcode'
print(firstUniqChar(test))