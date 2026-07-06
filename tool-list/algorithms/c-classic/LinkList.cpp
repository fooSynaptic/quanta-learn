/**
 * @file LinkList.cpp
 * @brief Singly Linked List implementation in C++
 * 
 * This file provides basic linked list operations including:
 * - Initialization
 * - Node insertion at head
 * - List traversal and printing
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
 * @brief Main function - demonstrates linked list operations
 */
int main()
{
    LinkNode* head = nullptr;
    
    init_list(head);
    
    /* Add nodes to the list (inserts at head, so order is reversed) */
    add_node(1, head);
    add_node(2, head);
    add_node(3, head);
    
    printf("Linked list contents: ");
    print_list(head);

    /* Clean up */
    free_list(head);
    head = nullptr;

    return 0;
}
