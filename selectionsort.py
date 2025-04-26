class Solution:
    # Function to perform selection sort on the given array
    def selectionSort(self, arr):
        n = len(arr)

        # Traverse through all elements in the array
        for i in range(n - 1):
            # Find the minimum element in the unsorted part of the array
            minIndex = i
            for j in range(i + 1, n):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            
            # Swap the found minimum element with the element at index 'i'
            if minIndex != i:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]


# Driver code to test the Solution
if __name__ == "__main__":
    solution = Solution()
    arr = [64, 25, 12, 22, 11]

    print("Original array:", arr)

    # Sort the array using selection sort
    solution.selectionSort(arr)

    print("Sorted array:", arr)
