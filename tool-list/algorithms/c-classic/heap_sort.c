/**
 * @file heap_sort.c
 * @brief Implementation of the Heap Sort algorithm in C
 * 
 * Heap Sort is a comparison-based sorting algorithm that uses a binary heap
 * data structure. It has O(n log n) time complexity for all cases and
 * O(1) space complexity (in-place sorting).
 */

#include <stdio.h>
#include <stdlib.h>

/* Constants */
#define ARRAY_SIZE 10

/* Function Prototypes */
void heapify(int arr[], int n, int root_idx);
void heap_sort(int arr[], int n);
void swap(int *a, int *b);
void print_array(const int arr[], int n);

/**
 * @brief Maintains the max heap property by ensuring parent is larger than children
 * 
 * @param arr Array to heapify
 * @param n Size of the heap
 * @param root_idx Index of the root element to heapify
 */
void heapify(int arr[], int n, int root_idx)
{
    int largest_idx = root_idx;        // Initialize largest as root
    int left_child_idx = 2 * root_idx + 1;   // Left child index
    int right_child_idx = 2 * root_idx + 2;  // Right child index

    /* If left child is larger than root */
    if (left_child_idx < n && arr[left_child_idx] > arr[largest_idx]) {
        largest_idx = left_child_idx;
    }

    /* If right child is larger than largest so far */
    if (right_child_idx < n && arr[right_child_idx] > arr[largest_idx]) {
        largest_idx = right_child_idx;
    }

    /* If largest is not root, swap and continue heapifying */
    if (largest_idx != root_idx) {
        swap(&arr[root_idx], &arr[largest_idx]);
        
        /* Recursively heapify the affected sub-tree */
        heapify(arr, n, largest_idx);
    }
}

/**
 * @brief Main heap sort function
 * 
 * @param arr Array to be sorted
 * @param n Size of the array
 */
void heap_sort(int arr[], int n)
{
    /* Build max heap: rearrange array to satisfy heap property */
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }

    /* Extract elements from heap one by one */
    for (int i = n - 1; i > 0; i--) {
        /* Move current root (maximum) to end */
        swap(&arr[0], &arr[i]);
        
        /* Call heapify on the reduced heap */
        heapify(arr, i, 0);
    }
}

/**
 * @brief Swaps two integer values
 * 
 * @param a Pointer to first integer
 * @param b Pointer to second integer
 */
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
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
        printf("%d ", arr[i]);
    }
    printf("\n");
}

/**
 * @brief Main function - demonstrates heap sort
 */
int main(void)
{
    int arr[ARRAY_SIZE] = {3, 1, 6, 7, 9, 5, 4, 2, 8, 0};

    printf("Original array: ");
    print_array(arr, ARRAY_SIZE);

    heap_sort(arr, ARRAY_SIZE);

    printf("Sorted array:   ");
    print_array(arr, ARRAY_SIZE);

    return 0;
}
