/**
 * @file palindrome_num.cpp
 * @brief Check if a linked list is a palindrome using a stack
 * 
 * Algorithm:
 * 1. Find the middle of the linked list using slow/fast pointers
 * 2. Push the first half of nodes onto a stack
 * 3. Compare the second half with elements popped from stack
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n) for the stack
 */

#include <cstdio>
#include <cstdlib>

/* Constants */
#define MAX_SIZE 100

/* Forward declarations */
struct LinkNode;
struct SqStack;

/**
 * @brief Node structure for singly linked list
 */
struct LinkNode {
    int data;           /**< Data stored in the node */
    LinkNode* next;     /**< Pointer to the next node */
};

/**
 * @brief Sequential Stack structure
 */
struct SqStack {
    LinkNode* data[MAX_SIZE];
    int length;
};

/* Function Prototypes for Linked List */
void init_list(LinkNode*& head);
void add_node(int value, LinkNode* head);
void print_list(const LinkNode* head);
void free_list(LinkNode* head);

/* Function Prototypes for Stack */
void init_stack(SqStack*& stack);
bool is_stack_empty(const SqStack* stack);
bool is_stack_full(const SqStack* stack);
void push(LinkNode* node, SqStack* stack);
bool pop(SqStack* stack, LinkNode*& node);
void free_stack(SqStack* stack);

/* Function Prototype for Palindrome Check */
bool is_palindrome_list(LinkNode* head);

/* ==================== Linked List Implementation ==================== */

void init_list(LinkNode*& head)
{
    head = (LinkNode*)malloc(sizeof(LinkNode));
    if (head == nullptr) {
        fprintf(stderr, "Error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    head->next = nullptr;
}

void add_node(int value, LinkNode* head)
{
    if (head == nullptr) {
        fprintf(stderr, "Error: List not initialized\n");
        return;
    }

    LinkNode* new_node = (LinkNode*)malloc(sizeof(LinkNode));
    if (new_node == nullptr) {
        fprintf(stderr, "Error: Memory allocation failed\n");
        return;
    }

    new_node->data = value;
    new_node->next = head->next;
    head->next = new_node;
}

void print_list(const LinkNode* head)
{
    if (head == nullptr) {
        return;
    }

    const LinkNode* current = head->next;
    while (current != nullptr) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

void free_list(LinkNode* head)
{
    if (head == nullptr) {
        return;
    }

    LinkNode* current = head;
    while (current != nullptr) {
        LinkNode* temp = current;
        current = current->next;
        free(temp);
    }
}

/* ==================== Stack Implementation ==================== */

void init_stack(SqStack*& stack)
{
    stack = (SqStack*)malloc(sizeof(SqStack));
    if (stack == nullptr) {
        fprintf(stderr, "Error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    stack->length = 0;
}

bool is_stack_empty(const SqStack* stack)
{
    if (stack == nullptr) {
        return true;
    }
    return (stack->length <= 0);
}

bool is_stack_full(const SqStack* stack)
{
    if (stack == nullptr) {
        return false;
    }
    return (stack->length >= MAX_SIZE);
}

void push(LinkNode* node, SqStack* stack)
{
    if (stack == nullptr || is_stack_full(stack)) {
        return;
    }
    stack->data[stack->length] = node;
    stack->length++;
}

bool pop(SqStack* stack, LinkNode*& node)
{
    if (stack == nullptr || is_stack_empty(stack)) {
        return false;
    }
    stack->length--;
    node = stack->data[stack->length];
    return true;
}

void free_stack(SqStack* stack)
{
    free(stack);
}

/* ==================== Palindrome Check ==================== */

/**
 * @brief Determines if a linked list is a palindrome
 * 
 * Uses the two-pointer technique to find the middle of the list,
 * then uses a stack to store the first half for comparison.
 * 
 * @param head Pointer to the head of the linked list
 * @return true if the list is a palindrome, false otherwise
 */
bool is_palindrome_list(LinkNode* head)
{
    if (head == nullptr || head->next == nullptr) {
        return false;  /* Empty list or single node (no next) is not considered palindrome */
    }

    LinkNode* slow_ptr = head;
    LinkNode* fast_ptr = head;
    SqStack* stack = nullptr;
    init_stack(stack);

    /* 
     * Fast pointer moves 2 steps while slow pointer moves 1 step.
     * When fast reaches end, slow is at the middle.
     * Push nodes visited by slow pointer onto stack.
     */
    while (fast_ptr->next != nullptr && fast_ptr->next->next != nullptr) {
        fast_ptr = fast_ptr->next->next;
        slow_ptr = slow_ptr->next;
        push(slow_ptr, stack);
    }

    /* If stack is empty, list has 0 or 1 nodes */
    if (is_stack_empty(stack)) {
        free_stack(stack);
        return false;
    }

    /* Determine if list has odd or even number of nodes */
    if (fast_ptr->next != nullptr) {
        /* Odd number of nodes, skip the middle node */
        slow_ptr = slow_ptr->next;
    }

    /* Compare second half with first half (from stack) */
    LinkNode* node_from_stack = nullptr;
    slow_ptr = slow_ptr->next;  /* Move to start of second half */

    while (slow_ptr != nullptr) {
        if (!pop(stack, node_from_stack)) {
            break;
        }
        /* If any node differs, it's not a palindrome */
        if (slow_ptr->data != node_from_stack->data) {
            free_stack(stack);
            return false;
        }
        slow_ptr = slow_ptr->next;
    }

    free_stack(stack);
    return true;
}

/* ==================== Main ==================== */

/**
 * @brief Main function - demonstrates palindrome list checking
 */
int main()
{
    LinkNode* head = nullptr;
    init_list(head);

    /* Create palindrome list: 2 -> 3 -> 3 -> 2 */
    add_node(2, head);
    add_node(3, head);
    add_node(3, head);
    add_node(2, head);

    printf("List contents: ");
    print_list(head);

    if (is_palindrome_list(head)) {
        printf("The list IS a palindrome.\n");
    } else {
        printf("The list is NOT a palindrome.\n");
    }

    /* Clean up */
    free_list(head);
    head = nullptr;

    return 0;
}
