def makeIncreasing(arr):
    operations = 0
    for i in range(1, len(arr)):
        prev = arr[i - 1]
        cur = arr[i]
        if cur <= prev:
            operations += (prev - cur) + 1
            arr[i] = prev + 1
    return operations


arr = [3, 1, 3, 0]
print(makeIncreasing(arr))