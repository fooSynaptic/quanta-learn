/**
 * @file longest_palindrom.h
 * @brief Header file for Longest Palindromic Substring algorithm
 * 
 * This file contains the Solution class that implements the algorithm
 * to find the longest palindromic substring in a given string using
 * dynamic programming.
 * 
 * Time Complexity: O(n²) where n is the length of the string
 * Space Complexity: O(n²) for the DP table
 */

#ifndef LONGEST_PALINDROM_H
#define LONGEST_PALINDROM_H

#define MAX_SIZE 1000

#include <string>
#include <iostream>
#include <climits>
#include <algorithm>

/**
 * @class Solution
 * @brief Class containing the longest palindrome algorithm
 * 
 * This class implements a dynamic programming solution to find the
 * longest palindromic substring in a given string.
 */
class Solution {
public:
    /**
     * @brief Finds the longest palindromic substring
     * 
     * Uses dynamic programming where dp[i][j] is true if substring
     * s[i..j] is a palindrome.
     * 
     * Base cases:
     * - Single characters are palindromes: dp[i][i] = true
     * - Two same characters are palindromes: dp[i][i+1] = (s[i] == s[i+1])
     * 
     * Recurrence:
     * - dp[i][j] = (s[i] == s[j]) && dp[i+1][j-1]
     * 
     * @param input_str The input string to search
     * @return std::string The longest palindromic substring found
     */
    std::string longest_palindrome(const std::string& input_str);

private:
    /**
     * @brief Prints the DP table for debugging purposes
     * 
     * @param dp_table Pointer to the DP table
     * @param n Size of the table (n x n)
     */
    void print_dp_table(const int* dp_table, int n);
};

/**
 * @brief Implementation of the longest palindrome algorithm
 */
inline std::string Solution::longest_palindrome(const std::string& input_str)
{
    int str_len = static_cast<int>(input_str.length());
    
    /* Handle empty string */
    if (str_len == 0) {
        return "";
    }
    
    /* Handle single character */
    if (str_len == 1) {
        return input_str;
    }

    std::string result_str = "";
    int max_length = 0;

    /* DP table: dp[i][j] = true if substring s[i..j] is palindrome */
    bool dp_table[MAX_SIZE][MAX_SIZE];
    
    /* For debugging purposes */
    int dp_backup[MAX_SIZE][MAX_SIZE];

    /* Initialize: all single characters are palindromes */
    for (int i = 0; i < str_len; i++) {
        dp_table[i][i] = true;
        dp_backup[i][i] = 1;
        
        /* Single character is a palindrome */
        if (max_length < 1) {
            result_str = input_str.substr(i, 1);
            max_length = 1;
        }
    }

    /* Fill the DP table */
    for (int end_pos = 1; end_pos < str_len; end_pos++) {
        for (int start_pos = 0; start_pos < end_pos; start_pos++) {
            
            /* Check if characters at positions match */
            if (input_str[start_pos] == input_str[end_pos]) {
                
                /* Case 1: Substring length <= 2 (adjacent or same char) */
                if (end_pos - start_pos <= 2) {
                    dp_table[start_pos][end_pos] = true;
                    dp_backup[start_pos][end_pos] = 1;
                    
                    int current_length = end_pos - start_pos + 1;
                    if (max_length < current_length) {
                        result_str = input_str.substr(start_pos, current_length);
                        max_length = current_length;
                    }
                }
                /* Case 2: Check inner substring */
                else if (dp_table[start_pos + 1][end_pos - 1]) {
                    dp_table[start_pos][end_pos] = true;
                    dp_backup[start_pos][end_pos] = 1;
                    
                    int current_length = end_pos - start_pos + 1;
                    if (max_length < current_length) {
                        result_str = input_str.substr(start_pos, current_length);
                        max_length = current_length;
                    }
                } else {
                    dp_table[start_pos][end_pos] = false;
                    dp_backup[start_pos][end_pos] = 0;
                }
            } else {
                dp_table[start_pos][end_pos] = false;
                dp_backup[start_pos][end_pos] = 0;
            }
        }
    }

    /* Print DP table for debugging */
    std::cout << "DP Table:" << std::endl;
    for (int i = 0; i < str_len; i++) {
        for (int j = 0; j < str_len; j++) {
            std::cout << dp_backup[i][j] << ' ';
        }
        std::cout << std::endl;
    }

    return result_str;
}

#endif /* LONGEST_PALINDROM_H */
