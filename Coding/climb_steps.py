"""
Climbing Stairs - Dynamic Programming Solution.

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

This is a classic dynamic programming problem similar to Fibonacci sequence.

Examples:
    Input: n = 2
    Output: 2
    Explanation: Two ways: 1+1 steps or 2 steps at once
    
    Input: n = 3
    Output: 3
    Explanation: Three ways: 1+1+1, 1+2, or 2+1

Time Complexity: O(n) for optimized solution, O(2^n) for naive recursive
Space Complexity: O(n) for array solution, O(1) for optimized solution
"""


class StairClimber:
    """Solutions for the climbing stairs problem."""
    
    def climb_stairs_recursive(self, n: int) -> int:
        """
        Naive recursive solution (inefficient for large n).
        
        Time: O(2^n) - exponential
        Space: O(n) - recursion stack
        
        Args:
            n: Number of steps to climb
            
        Returns:
            Number of distinct ways to climb
        """
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        return self.climb_stairs_recursive(n - 1) + self.climb_stairs_recursive(n - 2)
    
    def climb_stairs_memoized(self, n: int) -> int:
        """
        Memoized solution using top-down dynamic programming.
        
        Time: O(n)
        Space: O(n)
        
        Args:
            n: Number of steps to climb
            
        Returns:
            Number of distinct ways to climb
        """
        if n <= 1:
            return 1
            
        memo = {}
        
        def dp(step: int) -> int:
            if step <= 1:
                return 1
            if step in memo:
                return memo[step]
            memo[step] = dp(step - 1) + dp(step - 2)
            return memo[step]
        
        return dp(n)
    
    def climb_stairs_iterative(self, n: int) -> int:
        """
        Bottom-up dynamic programming with O(n) space.
        
        Time: O(n)
        Space: O(n)
        
        Args:
            n: Number of steps to climb
            
        Returns:
            Number of distinct ways to climb
        """
        if n <= 1:
            return 1
        
        # dp[i] represents ways to reach step i
        ways = [0] * (n + 1)
        ways[0] = 1  # One way to stay at ground
        ways[1] = 1  # One way to reach step 1
        
        for step in range(2, n + 1):
            ways[step] = ways[step - 1] + ways[step - 2]
        
        return ways[n]
    
    def climb_stairs_optimized(self, n: int) -> int:
        """
        Space-optimized iterative solution.
        
        Only need to keep track of the previous two values.
        
        Time: O(n)
        Space: O(1)
        
        Args:
            n: Number of steps to climb
            
        Returns:
            Number of distinct ways to climb
        """
        if n <= 1:
            return 1
        
        prev_prev = 1  # ways[i-2]
        prev = 2       # ways[i-1]
        
        for step in range(3, n + 1):
            current = prev + prev_prev
            prev_prev = prev
            prev = current
        
        return prev


# Alias for backward compatibility
Solution = StairClimber


if __name__ == "__main__":
    climber = StairClimber()
    
    # Test different solutions
    test_cases = [2, 3, 10, 38]
    
    print("Climbing Stairs Solutions:")
    print("-" * 50)
    
    for n in test_cases:
        print(f"\nn = {n}:")
        print(f"  Memoized:   {climber.climb_stairs_memoized(n)} ways")
        print(f"  Iterative:  {climber.climb_stairs_iterative(n)} ways")
        print(f"  Optimized:  {climber.climb_stairs_optimized(n)} ways")
