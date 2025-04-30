def bubbleSort(arr):
    arr = arr.copy()
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    import time
    import random
    start_time = time.time()
    arrs = [random.randint(0, 100) for i in range(10)]
    print("Original array is:")
    print(arrs)
    sorted_arr = bubbleSort(arrs)
    print("--- %s microsecond ---" % ((time.time() - start_time)*(1000**2)))
    print(sorted_arr)
