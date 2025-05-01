#include <vector>
void quickSort(std::vector<int>& arr, int left, int right) {
    if (left >= right) return;
    
    int pivot = arr[left + (right - left)/2]; // 中间基准
    int i = left, j = right;
    
    while (i <= j) {
        while (arr[i] < pivot) i++;
        while (arr[j] > pivot) j--;
        if (i <= j) {
            std::swap(arr[i], arr[j]);
            i++;
            j--;
        }
    }
    
    quickSort(arr, left, j);
    quickSort(arr, i, right);
}
