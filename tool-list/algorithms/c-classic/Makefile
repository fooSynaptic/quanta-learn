CC = gcc
CXX = g++
CFLAGS = -std=c99 -Wall -Wextra
CXXFLAGS = -std=c++17 -Wall -Wextra

C_TARGETS = heap_sort merge_sort
CPP_TARGETS = dijkstra linklist reverse_linklist sqstack longest_palmseq palindrome_num max test

.PHONY: all clean run-heap run-merge

all: $(C_TARGETS) $(CPP_TARGETS)

heap_sort: heap_sort.c
	$(CC) $(CFLAGS) -o $@ $<

merge_sort: merge_sort.c
	$(CC) $(CFLAGS) -o $@ $<

dijkstra: Dijkstra.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

linklist: LinkList.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

reverse_linklist: reverse_linklist.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

sqstack: SqStack.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

longest_palmseq: longest_palmseq.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

palindrome_num: palindrome_num.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

max: max.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

test: test.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

run-heap: heap_sort
	./heap_sort

run-merge: merge_sort
	./merge_sort

clean:
	rm -f $(C_TARGETS) $(CPP_TARGETS)
