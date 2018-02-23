
# Linear search algorithm

def search(arr, element):
    for number in range(len(arr)):
        if arr[number] == element:
            return number

    return -1

arr = [9, 7, 2, 4, 6, 1, 2]
element = 10
print(search(arr, element))
