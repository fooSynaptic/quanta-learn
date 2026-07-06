/**
 * @file SqStack.cpp
 * @brief Sequential Stack implementation using array
 * 
 * This file implements a stack data structure using a dynamically allocated array.
 * The stack follows LIFO (Last In, First Out) principle.
 * Maximum capacity is defined by MAX_SIZE.
 */

#include <cstdio>
#include <cstdlib>

/* Forward declaration for LinkNode */
struct LinkNode;

/* Constants */
#define MAX_SIZE 100

/**
 * @brief Sequential Stack structure using array
 */
struct SqStack {
    LinkNode* data[MAX_SIZE];   /**< Array to store stack elements */
    int length;                  /**< Current number of elements in stack */
};

/**
 * @brief Node structure (forward declaration from LinkList)
 */
struct LinkNode {
    int data;
    LinkNode* next;
};

/* Function Prototypes */
void init_stack(SqStack*& stack);
bool is_stack_empty(const SqStack* stack);
bool is_stack_full(const SqStack* stack);
void push(LinkNode* node, SqStack* stack);
bool pop(SqStack* stack, LinkNode*& node);
void free_stack(SqStack* stack);

/**
 * @brief Initializes an empty stack
 * 
 * @param stack Reference to stack pointer (will be allocated)
 */
void init_stack(SqStack*& stack)
{
    stack = (SqStack*)malloc(sizeof(SqStack));
    if (stack == nullptr) {
        fprintf(stderr, "Error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    stack->length = 0;
}

/**
 * @brief Checks if the stack is empty
 * 
 * @param stack Pointer to the stack
 * @return true if stack is empty, false otherwise
 */
bool is_stack_empty(const SqStack* stack)
{
    if (stack == nullptr) {
        return true;
    }
    return (stack->length <= 0);
}

/**
 * @brief Checks if the stack is full
 * 
 * @param stack Pointer to the stack
 * @return true if stack is full, false otherwise
 */
bool is_stack_full(const SqStack* stack)
{
    if (stack == nullptr) {
        return false;
    }
    return (stack->length >= MAX_SIZE);
}

/**
 * @brief Pushes a node onto the stack
 * 
 * @param node Pointer to the node to push
 * @param stack Pointer to the stack
 */
void push(LinkNode* node, SqStack* stack)
{
    if (stack == nullptr) {
        fprintf(stderr, "Error: Stack not initialized\n");
        return;
    }

    if (is_stack_full(stack)) {
        fprintf(stderr, "Error: Stack overflow\n");
        return;
    }

    stack->data[stack->length] = node;
    stack->length++;
}

/**
 * @brief Pops a node from the stack
 * 
 * @param stack Pointer to the stack
 * @param node Reference to store the popped node
 * @return true if pop was successful, false otherwise
 */
bool pop(SqStack* stack, LinkNode*& node)
{
    if (stack == nullptr) {
        return false;
    }

    if (is_stack_empty(stack)) {
        return false;
    }

    stack->length--;
    node = stack->data[stack->length];
    return true;
}

/**
 * @brief Frees memory allocated for the stack
 * 
 * @param stack Pointer to the stack
 */
void free_stack(SqStack* stack)
{
    free(stack);
}

/**
 * @brief Main function - demonstrates stack operations (when compiled standalone)
 * 
 * Note: This file is typically included by other files (like palindrome_num.cpp)
 * and the main function here is for testing purposes only.
 */
int main()
{
    SqStack* stack = nullptr;

    init_stack(stack);

    /* Create test nodes */
    LinkNode* node1 = (LinkNode*)malloc(sizeof(LinkNode));
    LinkNode* node2 = (LinkNode*)malloc(sizeof(LinkNode));
    
    if (node1 == nullptr || node2 == nullptr) {
        fprintf(stderr, "Error: Memory allocation failed\n");
        return EXIT_FAILURE;
    }

    node1->data = 10;
    node2->data = 20;

    /* Test push operations */
    printf("Pushing nodes...\n");
    push(node1, stack);
    push(node2, stack);
    printf("Stack size: %d\n", stack->length);

    /* Test pop operations */
    LinkNode* popped = nullptr;
    if (pop(stack, popped)) {
        printf("Popped node data: %d\n", popped->data);
    }

    /* Clean up */
    free(node1);
    free(node2);
    free_stack(stack);

    return 0;
}
