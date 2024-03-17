import math

def find_peak(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
            return arr[mid]
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

def square_root_of_peak(arr):
    return math.sqrt(find_peak(arr))

arr = [1, 3, 6, 8, 10, 9, 7, 5, 2]
peak = find_peak(arr)
print("Peak element:", peak)
square_root = square_root_of_peak(arr)
print("Square root of the peak element: %.2f"% square_root)
