def minima(arr):
    ans = []
    i = 0

    while i < len(arr) - 1:
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            ans.append(i)

    return ans
