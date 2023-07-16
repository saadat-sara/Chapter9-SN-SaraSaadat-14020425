import random

def linear_threshold_model(graph, thresholds, weights):
    active_set = set()  # Set of currently active nodes
    new_active_set = set()  # Set of nodes activated in the current step

    while True:
        for node in graph:
            if node in active_set:
                continue  # Node is already active

            total_weight = sum(weights[node][neighbor] for neighbor in graph[node] if neighbor in active_set)
            if total_weight >= thresholds[node]:
                new_active_set.add(node)

        if not new_active_set:  # No new nodes activated
            break

        active_set.update(new_active_set)
        new_active_set.clear()

    return active_set

def influence_maximization(graph, thresholds, weights, k):
    seeds = set()  # Set of seed nodes

    for _ in range(k):
        max_influence = -1
        max_node = None

        for node in graph:
            if node not in seeds:
                seeds.add(node)
                influence = len(linear_threshold_model(graph, thresholds, weights))
                seeds.remove(node)

                if influence > max_influence:
                    max_influence = influence
                    max_node = node

        seeds.add(max_node)

    return seeds

# Example usage
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

thresholds = {
    'A': 0.5,
    'B': 0.7,
    'C': 0.3,
    'D': 0.6
}

weights = {
    'A': {'B': 0.2, 'C': 0.3, 'D': 0.5},
    'B': {'C': 0.4, 'D': 0.1},
    'C': {'D': 0.6},
    'D': {}
}

k = 2

seeds = influence_maximization(graph, thresholds, weights, k)
print("Selected seeds:", seeds)