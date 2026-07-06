/**
 * @file test.cpp
 * @brief Test file for longest palindromic substring algorithm
 * 
 * This file tests the Solution class implementation from
 * longest_palindrom.h header file.
 */

#include <cstdlib>
#include <iostream>
#include <string>
#include "longest_palindrom.h"

using namespace std;

/**
 * @brief Main function - tests the longest palindrome solution
 * 
 * Creates a Solution object and tests it with the string "ababa".
 */
int main()
{
    Solution solution;
    
    std::string test_string = "ababa";
    std::string result = solution.longest_palindrome(test_string);
    
    printf("Input: %s\n", test_string.c_str());
    printf("Longest palindromic substring: %s\n", result.c_str());

    return 0;
}
