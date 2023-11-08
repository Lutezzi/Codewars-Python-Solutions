def minimum(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low

def maximum(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high