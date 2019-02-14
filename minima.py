def minima(arr):
    ans = []
    i = 0

    for i in range(len(arr) - 1):
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            ans.append(i)

    return ans

def maxima(arr):
    ans = []
    i = 0

    for i in range(len(arr) - 1):
        if arr[i-1] > arr[i] and arr[i] < arr[i+1]:
            ans.append(i)

    return ans


class Fake:
    def __init__(self):
        pass

    def func(self, x, y):
        return x + y
