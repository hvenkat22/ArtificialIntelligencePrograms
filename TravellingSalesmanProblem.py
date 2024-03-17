def tsp_dp(graph):
  n = len(graph)
  vertices = [i for i in range(n) if i != 0]
  memo = {}

  def tsp_helper(curr, visited):
      if len(visited) == n:
          return graph[curr][0], [0]

      if (curr, tuple(visited)) in memo:
          return memo[(curr, tuple(visited))]

      min_dist = float('inf')
      min_path = None

      for next_vert in vertices:
          if next_vert not in visited:
              dist, path = tsp_helper(next_vert, visited + [next_vert])
              total_dist = graph[curr][next_vert] + dist
              if total_dist < min_dist:
                  min_dist = total_dist
                  min_path = [curr] + path

      memo[(curr, tuple(visited))] = (min_dist, min_path)

      return min_dist, min_path

  min_distance, min_path = tsp_helper(0, [0])

  return min_distance, min_path

graph = [[0, 8, 6, 12], [8, 0, 15, 25], [6, 15, 0, 10], [12, 25, 10, 0]]

min_dist, min_path = tsp_dp(graph)
print("Minimum distance:", min_dist)
print("Optimal path:", min_path)