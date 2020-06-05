# // No. 3
# //Dogs don't get along with cats, and cats don't get along with dogs.
# //What they both have in common is that they don't get along with water (baths).
# //Given an array of 'dogs', 'cats', and 'water', write a function called separate,
# //which returns a new array so that the dogs are separated from the cats by water.
# // Make sure that cats always come first in the array.
#
# //You can assume that the array will always at least three elements, and
# //that there'll always be at least one dog, one cat, and one water to work with.
from collections import deque
def separate(arr):
    # mid = len(arr)/2
    deq = deque(maxlen=len(arr))
    if 'water' in arr:
        deq.append('water')
        arr.remove('water')

    for i in range(len(arr)):
        if arr[i] == 'dog':
            deq.append(arr[i])
        else:
            deq.appendleft(arr[i])
    return list(deq)


print(separate(['dog','cat','water','cat']))
