def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

if __name__ == '__main__':
    import time
    import random
    start_time = time.time()
    arrs = [random.randint(0, 100) for i in range(10)]
    print("Original array is:")
    print(arrs)
    sorted_arr = quickSort(arrs)
    print("--- %s microsecond ---" % ((time.time() - start_time)*(1000**2)))
    print(sorted_arr)
