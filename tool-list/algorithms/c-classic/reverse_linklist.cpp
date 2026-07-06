/**
 * @file reverse_linklist.cpp
 * @brief Linked List implementation with reversal operation
 * 
 * This file provides a complete singly linked list implementation
 * including initialization, node insertion, list printing, and
 * an in-place list reversal algorithm.
 */

#include <cstdio>
#include <cstdlib>

/* Constants */
#define MAX_SIZE 100

/**
 * @brief Node structure for singly linked list
 */
struct LinkNode {
    int data;           /**< Data stored in the node */
    LinkNode* next;     /**< Pointer to the next node */
};

/* Function Prototypes */
void init_list(LinkNode*& head);
void add_node(int value, LinkNode* head);
void print_list(const LinkNode* head);
void reverse_list(LinkNode* head);
void free_list(LinkNode* head);

/**
 * @brief Initializes an empty linked list with a dummy head node
 * 
 * @param head Reference to the head pointer (will be allocated)
 */
void init_list(LinkNode*& head)
{
    head = (LinkNode*)malloc(sizeof(LinkNode));
    if (head == nullptr) {
        fprintf(stderr, "Error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    head->next = nullptr;
}

/**
 * @brief Adds a new node with given value at the head of the list
 * 
 * @param value Integer value to store in the new node
 * @param head Pointer to the head of the list
 */
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

/**
 * @brief Prints all elements in the linked list
 * 
 * @param head Pointer to the head of the list
 */
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

/**
 * @brief Reverses a singly linked list in-place (iterative approach)
 * 
 * Uses three pointers to reverse the links between nodes:
 * - prev: points to the previous node
 * - current: points to the current node being processed
 * - next: temporarily stores the next node
 * 
 * @param head Pointer to the head of the list
 */
void reverse_list(LinkNode* head)
{
    if (head == nullptr || head->next == nullptr) {
        return;
    }

    LinkNode* current = head->next;   /* First actual node */
    LinkNode* prev = nullptr;          /* Will become the new tail */
    LinkNode* next = nullptr;          /* Temporarily stores next node */

    /* Reverse the links between nodes */
    while (current != nullptr) {
        next = current->next;      /* Save next node */
        current->next = prev;      /* Reverse the link */
        prev = current;            /* Move prev forward */
        current = next;            /* Move current forward */
    }

    /* Update head to point to the new first node */
    head->next = prev;
}

/**
 * @brief Frees all memory allocated for the linked list
 * 
 * @param head Pointer to the head of the list
 */
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

/**
 * @brief Main function - demonstrates linked list reversal
 */
int main()
{
    LinkNode* head = nullptr;

    init_list(head);

    /* Create list: 4 -> 3 -> 2 -> 1 (due to head insertion) */
    add_node(1, head);
    add_node(2, head);
    add_node(3, head);
    add_node(4, head);

    printf("Original list: ");
    print_list(head);

    reverse_list(head);

    printf("Reversed list: ");
    print_list(head);

    /* Clean up */
    free_list(head);
    head = nullptr;

    return 0;
}
