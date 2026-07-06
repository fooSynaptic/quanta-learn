/**
 * @file max.cpp
 * @brief Find the largest element in an array
 * 
 * This program demonstrates finding the maximum element in an integer array
 * using C++ STL algorithms and standard C++ practices.
 */

#include <cstdlib>
#include <iostream>
#include <climits>
#include <algorithm>

using namespace std;

/**
 * @brief Finds the largest element in an integer array
 * 
 * Uses the STL max_element algorithm for efficient searching.
 * 
 * @param nums Array of integers
 * @param n Number of elements in the array
 * @return int The largest element in the array
 */
int find_largest(const int nums[], int n)
{
    if (n <= 0 || nums == nullptr) {
        cerr << "Error: Invalid array or size" << endl;
        return INT_MIN;
    }
    
    /* Use STL max_element which returns iterator to max element */
    return *max_element(nums, nums + n);
}

/**
 * @brief Prints an array to stdout
 * 
 * @param nums Array of integers
 * @param n Number of elements
 */
void print_array(const int nums[], int n)
{
    cout << "[";
    for (int i = 0; i < n; i++) {
        cout << nums[i];
        if (i < n - 1) {
            cout << ", ";
        }
    }
    cout << "]";
}

/**
 * @brief Main function - demonstrates finding maximum element
 */
int main()
{
    /* Sample array */
    const int nums[] = {5, 4, 9, 12, 8};
    const int n = sizeof(nums) / sizeof(nums[0]);

    cout << "Original array: ";
    print_array(nums, n);
    cout << endl;

    int largest = find_largest(nums, n);
    
    if (largest != INT_MIN) {
        cout << "Largest element of the array: " << largest << endl;
    }

    return 0;
}
