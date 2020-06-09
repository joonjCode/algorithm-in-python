# bubble sort
# given an array of numbers, sort them without using your language’s built in .sort method
# input: [4, 7, 2, 3, 8]
# output: [2, 3, 4, 7, 8]

# Bubble sort a.k.a sinking sort : compare adjacent elements and swap

def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        print('i',i)
        for j in range(i):
            print('j',j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

t = [4, 7, 2, 3, 8]
print(bubbleSort(t))
