"""
Problem
check for valid palindrome
only lowercase and number
"""


# Using List only
# def is_palindrom(s: str) -> bool:
#     strs = []
#     # Using deque
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#
#     while len(strs) > 1:
#         if strs.pop(0) != strs.pop():
#             return False
#     return True


# Using Deque only
from collections import deque


def is_palindrom(s: str) -> bool:
    strs = deque([])

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

#  Slicing
import re
def is_palindrom(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]

test = 'race a car'
test2 = 'A man, a plan, a canal: Panama'

print(is_palindrom(test))
print(is_palindrom(test2))
