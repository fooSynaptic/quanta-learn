# C Classic Algorithms

Classic C/C++ algorithm implementations migrated from the standalone repo
[`fooSynaptic/C-algorithm`](https://github.com/fooSynaptic/C-algorithm) into
`synaptic-learn` as a reusable `tool-list` module.

## Included Algorithms

### Sorting

| File | Description |
|------|-------------|
| `heap_sort.c` | In-place heap sort, `O(n log n)` |
| `merge_sort.c` | Stable merge sort, `O(n log n)` |

### Graph

| File | Description |
|------|-------------|
| `Dijkstra.cpp` | Shortest path on a weighted adjacency matrix |

### Data Structures

| File | Description |
|------|-------------|
| `LinkList.cpp` | Singly linked list |
| `reverse_linklist.cpp` | Linked list reversal |
| `SqStack.cpp` | Sequential stack backed by an array |

### String / Linked List Problems

| File | Description |
|------|-------------|
| `longest_palindrom.h` | Longest palindromic substring (DP, header-only) |
| `longest_palmseq.cpp` | Demo driver for the palindrome DP solution |
| `palindrome_num.cpp` | Check whether a linked list is a palindrome |
| `test.cpp` | Small test harness for `longest_palindrom.h` |

### Utility

| File | Description |
|------|-------------|
| `max.cpp` | Find the maximum element in an array |

## Build

```bash
cd tool-list/algorithms/c-classic
make
```

Run individual demos:

```bash
./heap_sort
./merge_sort
./dijkstra
./reverse_linklist
./longest_palmseq
```

Clean build artifacts:

```bash
make clean
```

## Manual Compilation

```bash
gcc -std=c99 -Wall -o heap_sort heap_sort.c
gcc -std=c99 -Wall -o merge_sort merge_sort.c
g++ -std=c++17 -Wall -o dijkstra Dijkstra.cpp
g++ -std=c++17 -Wall -o test test.cpp
```

## Complexity Summary

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| Heap Sort | `O(n log n)` | `O(1)` | Not stable |
| Merge Sort | `O(n log n)` | `O(n)` | Stable |
| Dijkstra | `O(V²)` | `O(V²)` | Adjacency matrix version |

## Catalog Registration

This module is registered as `tool-c-classic` by
`scripts/sync_catalog_from_legacy.py`. After syncing:

```bash
python3 scripts/sync_catalog_from_legacy.py
```

## Notes

- Some files retain Chinese comments from the original educational repo.
- Python sorting / heap utilities also exist under `tool-list/algorithms/sorting/`
  and `tool-list/algorithms/heapsort/`; this directory keeps the original C/C++
  reference implementations together.

## License

Educational use. Original repo: [fooSynaptic/C-algorithm](https://github.com/fooSynaptic/C-algorithm).
