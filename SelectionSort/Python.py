# This is the Python implementation of the selection sort algorithm.
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == '__main__':
    import time
    start_time = time.time()
    sarr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array is:")
    print(sarr)
    sorted_arr = selectionSort(sarr)
    print(sorted_arr)
    print("--- %s microsecond ---" % ((time.time() - start_time)*(1000**2)))
    print(sorted_arr)