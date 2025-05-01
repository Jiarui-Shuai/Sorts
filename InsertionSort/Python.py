# Insertion Sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == '__main__':
    import time
    import random
    start_time = time.time()
    arrs = [random.randint(0, 100) for i in range(10)]
    print("Original array is:")
    print(arrs)
    sorted_arr = insertionSort(arrs)
    print("--- %s microsecond ---" % ((time.time() - start_time)*(1000**2)))
    print(sorted_arr)