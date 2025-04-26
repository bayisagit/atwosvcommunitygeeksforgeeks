class Solution {
  public:
    // Function to perform selection sort on the given array.
    void selectionSort(vector<int> &arr) {
        // code here
                int n = arr.size();
        
        // Traverse through all elements in the array
        for (int i = 0; i < n - 1; ++i) {
            // Find the minimum element in the unsorted part of the array
            int minIndex = i;
            for (int j = i + 1; j < n; ++j) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            
            // Swap the found minimum element with the element at index 'i'
            if (minIndex != i) {
                swap(arr[i], arr[minIndex]);
            }
        }
    }
};