
def contains_cycle(first_node):
    nodes_visited = set()
    if not first_node or not first_node.next:
        return False
    current_node = first_node.next

    while current_node.next:
        if current_node.value in nodes_visited:
            return True
        else:
            nodes_visited.add(current_node.value)
            current_node = current_node.next
    return False
