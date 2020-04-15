def depth(tree_node):
  # our "queue" will store nodes at each level
  if tree_node is None:
    return 0
  # loop as long as there are nodes to explore
  else:
    left_depth=depth(tree_node["left_child"])
    # count the number of child nodes
    right_depth = depth(tree_node["right_child"])
    if left_depth > right_depth:
      return left_depth+1
    else:
      return right_depth+1
def depth(tree):
  result = 0
  # our "queue" will store nodes at each level
  queue = [tree]
  # loop as long as there are nodes to explore
  while queue:
    # count the number of child nodes
    level_count = len(queue)
    for child_count in range(0, level_count):
      # loop through each child
      child = queue.pop(0)
     # add its children if they exist
      if child["left_child"]:
        queue.append(child["left_child"])
      if child["right_child"]:
        queue.append(child["right_child"])
    # count the level
    result += 1
  return result
      
