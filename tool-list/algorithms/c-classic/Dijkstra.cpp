/**
 * @file Dijkstra.cpp
 * @brief Dijkstra's Shortest Path Algorithm Implementation
 * 
 * Dijkstra's algorithm finds the shortest path from a source vertex to all
 * other vertices in a weighted graph with non-negative edge weights.
 * 
 * Time Complexity: O(V²) where V is the number of vertices
 * (Can be improved to O(E + V log V) with a min-heap)
 * 
 * Space Complexity: O(V²) for the adjacency matrix representation
 */

#include <iostream>
#include <climits>
#include <algorithm>

/* Constants */
#define MAX_VERTICES 10
#define INFINITE_DISTANCE INT_MAX / 2  /* Use large value to avoid overflow */

/* Global arrays for Dijkstra's algorithm */
int distance_arr[MAX_VERTICES];      /**< Shortest distance from source to each vertex */
int predecessor_arr[MAX_VERTICES];   /**< Predecessor of each vertex in shortest path */
int adjacency_matrix[MAX_VERTICES][MAX_VERTICES];  /**< Graph represented as adjacency matrix */

/**
 * @brief Initializes the adjacency matrix with sample data
 * 
 * This is a placeholder - in practice, the graph would be loaded
 * from input or file.
 */
void init_graph()
{
    /* Initialize with zeros (no edges) */
    for (int i = 0; i < MAX_VERTICES; i++) {
        for (int j = 0; j < MAX_VERTICES; j++) {
            adjacency_matrix[i][j] = (i == j) ? 0 : INFINITE_DISTANCE;
        }
    }
    /* Add sample edges here if needed for testing */
}

/**
 * @brief Dijkstra's shortest path algorithm
 * 
 * Finds the shortest path from the source vertex to all other vertices.
 * Uses a greedy approach, always selecting the unvisited vertex with
 * the smallest tentative distance.
 * 
 * @param source_vertex The starting vertex for path calculations
 */
void dijkstra_shortest_path(int source_vertex)
{
    bool visited[MAX_VERTICES] = {false};  /* Track visited vertices */
    int num_vertices = MAX_VERTICES;

    /* Initialize distances and predecessors */
    for (int i = 0; i < num_vertices; ++i) {
        distance_arr[i] = adjacency_matrix[source_vertex][i];
        visited[i] = false;
        
        if (distance_arr[i] == INFINITE_DISTANCE) {
            predecessor_arr[i] = -1;  /* No path from source */
        } else {
            predecessor_arr[i] = source_vertex;
        }
    }

    /* Distance to source is 0 */
    distance_arr[source_vertex] = 0;
    visited[source_vertex] = true;

    /* Find shortest path for all remaining vertices */
    for (int i = 1; i < num_vertices; i++) {
        /* Find the unvisited vertex with minimum distance */
        int min_distance = INFINITE_DISTANCE;
        int min_vertex = source_vertex;

        for (int v = 0; v < num_vertices; ++v) {
            if (!visited[v] && distance_arr[v] < min_distance) {
                min_vertex = v;
                min_distance = distance_arr[v];
            }
        }

        /* Mark the selected vertex as visited */
        visited[min_vertex] = true;

        /* Update distances to neighbors of the selected vertex */
        for (int v = 0; v < num_vertices; v++) {
            if (!visited[v] && adjacency_matrix[min_vertex][v] != INFINITE_DISTANCE) {
                int new_distance = distance_arr[min_vertex] + adjacency_matrix[min_vertex][v];
                
                /* If found a shorter path, update distance and predecessor */
                if (new_distance < distance_arr[v]) {
                    distance_arr[v] = new_distance;
                    predecessor_arr[v] = min_vertex;
                }
            }
        }
    }
}

/**
 * @brief Prints the shortest path from source to a target vertex
 * 
 * @param target_vertex The destination vertex
 * @param source_vertex The source vertex (for stopping condition)
 */
void print_path(int target_vertex, int source_vertex)
{
    if (target_vertex == source_vertex) {
        std::cout << source_vertex;
        return;
    }
    if (predecessor_arr[target_vertex] == -1) {
        std::cout << "No path exists";
        return;
    }
    print_path(predecessor_arr[target_vertex], source_vertex);
    std::cout << " -> " << target_vertex;
}

/**
 * @brief Main function demonstrating Dijkstra's algorithm
 * 
 * Note: This implementation requires manual initialization of the
 * adjacency matrix before running the algorithm.
 */
int main()
{
    /* Initialize graph - add your edge weights here */
    init_graph();
    
    /* Example: Create a simple graph */
    /* Vertex 0 to 1 with weight 4 */
    adjacency_matrix[0][1] = 4;
    adjacency_matrix[1][0] = 4;
    
    /* Vertex 0 to 2 with weight 2 */
    adjacency_matrix[0][2] = 2;
    adjacency_matrix[2][0] = 2;
    
    /* Vertex 1 to 2 with weight 1 */
    adjacency_matrix[1][2] = 1;
    adjacency_matrix[2][1] = 1;
    
    /* Vertex 1 to 3 with weight 5 */
    adjacency_matrix[1][3] = 5;
    adjacency_matrix[3][1] = 5;
    
    /* Vertex 2 to 3 with weight 8 */
    adjacency_matrix[2][3] = 8;
    adjacency_matrix[3][2] = 8;

    int source = 0;
    dijkstra_shortest_path(source);

    /* Print results */
    std::cout << "Shortest distances from vertex " << source << ":" << std::endl;
    for (int i = 0; i < MAX_VERTICES; i++) {
        if (distance_arr[i] != INFINITE_DISTANCE) {
            std::cout << "To vertex " << i << ": distance = " << distance_arr[i];
            std::cout << ", path: ";
            print_path(i, source);
            std::cout << std::endl;
        }
    }

    return 0;
}
