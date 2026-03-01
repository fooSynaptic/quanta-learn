# Exam - Algorithm Practice Repository <img src=".github/icons/note.svg" width="16" height="16" alt="note">

A collection of algorithm implementations and solutions to coding problems from various sources including LeetCode, "Introduction to Algorithms" (CLRS), and computer science coursework.

## <img src=".github/icons/book.svg" width="16" height="16" alt="book"> Overview

This repository contains my solutions to data structure and algorithm problems, with a focus on:
- Classic algorithm implementations
- Data structure manipulations
- Interview preparation problems
- Time and space complexity analysis

## <img src=".github/icons/card_index.svg" width="16" height="16" alt="card index"> Repository Structure

```
exam/
├── Coding/                   # Algorithm implementations
│   ├── binary_insert.py     # Binary insertion algorithm
│   ├── Bucket_sort.py       # Bucket sort implementation
│   ├── build_binary_tree.py # Construct binary tree from traversals
│   ├── canFinish.py         # Course schedule (topological sort)
│   ├── check_palim.py       # Palindrome checking
│   ├── climb_steps.py       # Climbing stairs (Fibonacci variant)
│   ├── combine.py           # Combinations generation
│   ├── common_ancestry.py   # Lowest common ancestor
│   ├── common_prefix.py     # Longest common prefix
│   ├── countPrime.py        # Count prime numbers
│   ├── Dijkstra_Floyd.py    # Shortest path algorithms
│   ├── LCS_string.py        # Longest common subsequence
│   ├── merge_link_list.py   # Merge sorted linked lists
│   ├── reverse_link_list.py # Linked list reversal
│   ├── rotate_matrix.py     # Matrix rotation
│   ├── top_k.py             # Top K elements
│   ├── Trie.py              # Trie data structure
│   └── ...                  # Many more algorithms
├── combination/             # Combination-related experiments
│   ├── test.c               # C implementation
│   └── .env/                # Python virtual environment
└── interviewProblem/        # Interview problem solutions
```

## <img src=".github/icons/rocket.svg" width="16" height="16" alt="rocket"> Getting Started

### Prerequisites
- Python 3.6+
- (Optional) Virtual environment for isolated dependencies

### Running Solutions

```bash
# Run a specific solution
python Coding/climb_steps.py

# Run with Python 3 explicitly
python3 Coding/binary_insert.py
```

## <img src=".github/icons/book.svg" width="16" height="16" alt="book"> Topics Covered

### Data Structures
- **Arrays and Strings**: Sorting, searching, manipulation
- **Linked Lists**: Reversal, merging, fast-slow pointer techniques
- **Trees and Graphs**: Binary trees, BST validation, graph traversal
- **Heaps**: Priority queues, top-k problems
- **Hash Tables**: Frequency counting, two-sum patterns
- **Tries**: Prefix-based string storage

### Algorithms

#### Sorting
- Bucket Sort
- Binary Insertion
- Linked List Sort

#### Graph Algorithms
- Dijkstra's Shortest Path
- Floyd-Warshall
- Topological Sort (Course Schedule)
- Cycle Detection

#### Dynamic Programming
- Climbing Stairs (Fibonacci)
- Longest Common Subsequence (LCS)
- Maximum Subarray
- Coin Change Variants

#### Tree Operations
- Build tree from preorder/inorder
- Serialize/Deserialize
- Maximum subtree sum
- Validate balanced BST

#### String Algorithms
- Longest Common Prefix
- Word Search (Backtracking)
- Regular Expression Matching
- Palindrome Checking

#### Mathematical
- Prime Counting (Sieve)
- Matrix Rotation
- Random Number Generation
- Permutations

## <img src=".github/icons/bulb.svg" width="16" height="16" alt="bulb"> Problem Sources

- [LeetCode](https://leetcode.com) - Primary source
- [Introduction to Algorithms](https://mitpress.mit.edu/books/introduction-algorithms) (CLRS)
- [Mathematics in Computer Science](https://link.springer.com/journal/11786)

## <img src=".github/icons/target.svg" width="16" height="16" alt="target"> Interview Problems

Special section dedicated to interview preparation:
- Object serialization/deserialization
- System design considerations
- Edge case handling

## 📝 Code Style

This repository follows these conventions:
- **Python**: PEP 8 style guide
- **Functions**: snake_case naming
- **Classes**: PascalCase naming
- **Constants**: UPPER_SNAKE_CASE
- **Docstrings**: Google-style documentation

## <img src=".github/icons/search.svg" width="16" height="16" alt="search"> Example Usage

```python
# Building a binary tree from traversals
from build_binary_tree import Solution, TreeNode

solution = Solution()
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
tree = solution.buildTree(preorder, inorder)

# Climbing stairs (dynamic programming)
from climb_steps import Solution
solution = Solution()
ways = solution.climbStairs2(38)  # Efficient O(n) solution
```

## 🤝 Contributing

This is a personal learning repository. While not actively seeking contributions, 
feel free to fork and adapt for your own learning!

## 📄 License

For educational purposes only.
