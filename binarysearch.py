# Binary Search Algorithm
# TO DO
# pass the array
# Add case where 1 element

#import sys

arr = [5, 17, 23, 33, 39, 44, 58, 62, 70, 74, 82, 99]
end = len(arr)
start = 0
#sys.setrecursionlimit(40000)

def binarySearch(arr, start, end,  x):

   #print("This is end: {}".format(end))
    mid = int((end + start)/2)
    #print("This is start {}".format(start))
    #print("This is end {}".format(end))
    #print("This is mid {}".format(mid))

    #if x not in arr:
       #return None
    if start <= end: # base case
        if x == arr[mid]:
            return x
        elif (x < arr[mid]):
            start = start
            end = mid - 1
            return binarySearch(arr, start, end, x)
        else: # if x > arr[mid]
            start = mid + 1
            end = end
            return binarySearch(arr, start, end,  x)


position = binarySearch(arr, 0, 12, 5)
print(position)

