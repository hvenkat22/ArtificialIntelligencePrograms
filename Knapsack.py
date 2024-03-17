def knapsack(weights, values, capacity):
  n = len(values)
  # Create a 2D list to store the maximum values that can be achieved
  # for each subproblem
  dp = [[0] * (capacity + 1) for _ in range(n + 1)]

  # Fill the dp table
  for i in range(1, n + 1):
      for w in range(1, capacity + 1):
          if weights[i - 1] <= w:
              dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
          else:
              dp[i][w] = dp[i - 1][w]

  # Trace back to find the items included in the knapsack
  included_items = []
  w = capacity
  for i in range(n, 0, -1):
      if dp[i][w] != dp[i - 1][w]:
          included_items.append(i - 1)
          w -= weights[i - 1]

  return dp[n][capacity], included_items

weights = [2, 3, 4, 5,9,1,6]
values = [3, 4, 5, 6,1,9,2]
capacity = 7
max_value, included_items = knapsack(weights, values, capacity)

# Print the results
print("Maximum value:", max_value)
print("Items included:")
for item_index in included_items:
    print("Item", item_index + 1, ": Weight =", weights[item_index], ", Value =", values[item_index])