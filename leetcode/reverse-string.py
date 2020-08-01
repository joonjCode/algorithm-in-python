'''
Reverse a string without return
'''

# Using two pointers
def reverse_string(arr:list) -> None:
        left, right = 0, len(arr) - 1
        while left<right:
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right -=1

# Simpler version
def reverse_string2(arr: list) -> None:
    # arr.reverse()
    arr[:] = arr[::-1]




arr = ['h','e','l','l','o']
reverse_string(arr)
print(arr)


arr2 = ['h','e','l','l','o','2']
reverse_string2(arr2)
print(arr2)

