/**
 * @file longest_palmseq.cpp
 * @brief Main program to test Longest Palindromic Substring algorithm
 * 
 * This program demonstrates the usage of the Solution class to find
 * the longest palindromic substring in a given string.
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include "longest_palindrom.h"

using namespace std;

/**
 * @brief Main function - demonstrates longest palindrome algorithm
 * 
 * Tests the algorithm with the string "ababa" which should return
 * "ababa" itself (the entire string is a palindrome).
 */
int main()
{
    Solution solution;
    
    /* Test string */
    std::string test_str = "ababa";
    
    std::cout << "Input string: " << test_str << std::endl;
    std::string result = solution.longest_palindrome(test_str);
    
    std::cout << "Longest palindromic substring: " << result << std::endl;

    return 0;
}
