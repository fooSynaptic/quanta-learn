"""
Binary Insertion Algorithm with Performance Comparison.

This module implements binary insertion for maintaining a sorted list,
along with performance comparisons between different insertion methods.

The binary insertion algorithm finds the correct position for a new element
in a sorted array using binary search (O(log n)), then inserts it (O(n)).
Overall complexity: O(n) for a single insertion.
"""

import random
import time
from typing import List, Callable


class BinaryInserter:
    """Performs binary insertion into a sorted list."""
    
    def __init__(self):
        """Initialize with an empty sorted list."""
        self.sorted_list: List[int] = []
    
    def reset(self, initial_list: List[int] = None) -> None:
        """Reset the sorted list."""
        self.sorted_list = list(initial_list) if initial_list else []
    
    def binary_insert(self, target: int) -> None:
        """
        Insert target into sorted_list maintaining sorted order.
        
        Uses binary search to find the insertion point, then inserts.
        
        Args:
            target: The value to insert
        """
        if not self.sorted_list:
            self.sorted_list.append(target)
            return
        
        if target <= self.sorted_list[0]:
            self.sorted_list.insert(0, target)
            return
        
        if target >= self.sorted_list[-1]:
            self.sorted_list.append(target)
            return
        
        # Binary search for insertion point
        left, right = 0, len(self.sorted_list) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.sorted_list[mid] == target:
                # Exact match found, insert here
                self.sorted_list.insert(mid, target)
                return
            elif self.sorted_list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Insert at the correct position
        self.sorted_list.insert(left, target)


def timer_decorator(func: Callable, iterations: int = 1000) -> Callable:
    """
    Decorator to measure execution time of a function.
    
    Args:
        func: Function to time
        iterations: Number of iterations to run
        
    Returns:
        Wrapped function that prints timing information
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        for _ in range(iterations):
            result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"  {func.__name__}: {elapsed:.6f}s ({iterations} iterations)")
        return result
    return wrapper


def measure_insertion_performance(array: List[int], value: int, position: int) -> None:
    """
    Compare performance of different insertion methods.
    
    Args:
        array: Base array to work with
        value: Value to insert
        position: Position to insert at
    """
    print(f"\nPerformance comparison (inserting at position {position}):")
    
    # Method 1: list.insert()
    def method_insert():
        arr = list(array)
        arr.insert(position, value)
        return arr
    
    # Method 2: Slice concatenation
    def method_slice():
        return array[:position] + [value] + array[position:]
    
    timed_insert = timer_decorator(method_insert, 10000)
    timed_slice = timer_decorator(method_slice, 10000)
    
    timed_insert()
    timed_slice()


if __name__ == "__main__":
    # Demonstration of binary insertion
    print("Binary Insertion Demonstration")
    print("=" * 50)
    
    inserter = BinaryInserter()
    
    # Initial sorted array
    initial = [1, 5, 6, 10, 11, 11, 12, 13, 15, 17]
    inserter.reset(initial)
    print(f"Initial array: {inserter.sorted_list}")
    
    # Insert various values
    values_to_insert = [14, 0, 20, 7]
    
    for value in values_to_insert:
        print(f"\nInserting {value}:")
        inserter.binary_insert(value)
        print(f"Result: {inserter.sorted_list}")
        
        # Verify sorted order
        is_sorted = all(inserter.sorted_list[i] <= inserter.sorted_list[i + 1] 
                       for i in range(len(inserter.sorted_list) - 1))
        print(f"Sorted check: {'✓' if is_sorted else '✗'}")
    
    # Performance comparison
    print("\n" + "=" * 50)
    large_array = [random.randint(1, 10000) for _ in range(10000)]
    measure_insertion_performance(large_array, 5000, 5000)
