"""from collections import deque

def bfs(matrix, start):
    # Define the directions to move in the matrix
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Initialize the visited set and the queue
    visited = set()
    queue = deque([start])

    # Loop until the queue is empty
    while queue:
        # Dequeue the next node
        curr = queue.popleft()

        # Check if we have visited this node before
        if curr in visited:
            continue

        # Mark the current node as visited
        visited.add(curr)

        # Process the current node
        print(curr)

        # Add the unvisited neighbors of the current node to the queue
        for d in directions:
            neighbor = (curr[0] + d[0], curr[1] + d[1])
            if 0 <= neighbor[0] < len(matrix) and 0 <= neighbor[1] < len(matrix[0]) and matrix[neighbor[0]][neighbor[1]] != '#' and neighbor not in visited:
                queue.append(neighbor)

"""
import random

"""def add_random_chars(string):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(3):
        random_char = random.choice(chars)
        string += random_char
    return string

# example usage
my_string = "hello world"
my_string_with_random_chars = add_random_chars(my_string)
print(my_string_with_random_chars)



my_string = "hello world Baby"
min_length = 3  # minimum length of the substring
max_length = len(my_string) - 1  # maximum length of the substring
last_index = random.randint(min_length, max_length)
result = my_string[3:last_index]
print(result)  # prints a random substring of my_string starting at index 3
"""