/**
 * @file merge_sort.c
 * @brief Implementation of the Merge Sort algorithm in C
 * 
 * Merge Sort is a divide-and-conquer algorithm that divides the input array
 * into two halves, recursively sorts them, and then merges the two sorted halves.
 * Time Complexity: O(n log n) for all cases
 * Space Complexity: O(n) - requires additional space for merging
 */

#include <stdio.h>
#include <stdlib.h>

/* Constants */
#define ARRAY_SIZE 8

/* Function Prototypes */
void merge_sort(int arr[], int left_idx, int right_idx);
void merge(int arr[], int left_idx, int mid_idx, int right_idx);
void print_array(const int arr[], int n);

/**
 * @brief Merges two sorted subarrays into a single sorted subarray
 * 
 * First subarray: arr[left_idx..mid_idx]
 * Second subarray: arr[mid_idx+1..right_idx]
 * 
 * @param arr Array containing the subarrays
 * @param left_idx Starting index of the first subarray
 * @param mid_idx Ending index of the first subarray
 * @param right_idx Ending index of the second subarray
 */
void merge(int arr[], int left_idx, int mid_idx, int right_idx)
{
    int i, j, k;
    int left_size = mid_idx - left_idx + 1;
    int right_size = right_idx - mid_idx;

    /* Create temporary arrays */
    int left_arr[left_size];
    int right_arr[right_size];

    /* Copy data to temporary arrays */
    for (i = 0; i < left_size; i++) {
        left_arr[i] = arr[left_idx + i];
    }
    for (j = 0; j < right_size; j++) {
        right_arr[j] = arr[mid_idx + 1 + j];
    }

    /* Merge the temporary arrays back into arr[left_idx..right_idx] */
    i = 0;      /* Initial index of left subarray */
    j = 0;      /* Initial index of right subarray */
    k = left_idx;   /* Initial index of merged subarray */

    while (i < left_size && j < right_size) {
        if (left_arr[i] <= right_arr[j]) {
            arr[k] = left_arr[i];
            i++;
        } else {
            arr[k] = right_arr[j];
            j++;
        }
        k++;
    }

    /* Copy remaining elements of left_arr[], if any */
    while (i < left_size) {
        arr[k] = left_arr[i];
        i++;
        k++;
    }

    /* Copy remaining elements of right_arr[], if any */
    while (j < right_size) {
        arr[k] = right_arr[j];
        j++;
        k++;
    }
}

/**
 * @brief Main merge sort function (recursive)
 * 
 * @param arr Array to be sorted
 * @param left_idx Left index of the subarray
 * @param right_idx Right index of the subarray
 */
void merge_sort(int arr[], int left_idx, int right_idx)
{
    if (left_idx < right_idx) {
        /* Find the middle point to divide array into two halves */
        int mid_idx = left_idx + (right_idx - left_idx) / 2;

        /* Recursively sort first and second halves */
        merge_sort(arr, left_idx, mid_idx);
        merge_sort(arr, mid_idx + 1, right_idx);

        /* Merge the sorted halves */
        merge(arr, left_idx, mid_idx, right_idx);
    }
}

/**
 * @brief Prints an array to stdout
 * 
 * @param arr Array to print
 * @param n Size of the array
 */
void print_array(const int arr[], int n)
{
    for (int i = 0; i < n; i++) {
        printf("%d\n", arr[i]);
    }
}

/**
 * @brief Main function - demonstrates merge sort
 */
int main(void)
{
    int arr[ARRAY_SIZE] = {1, 6, 5, 4, 2, 7, 3, 8};

    printf("Original array:\n");
    print_array(arr, ARRAY_SIZE);

    merge_sort(arr, 0, ARRAY_SIZE - 1);

    printf("\nSorted array:\n");
    print_array(arr, ARRAY_SIZE);

    return 0;
}
