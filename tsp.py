def travellingsalesman(c):
  global cost
  adj_vertex = 999
  min_val = 999
  visited[c] = 1
  print((c + 1), end=" ")
  for k in range(n) :
      if (tsp_g[c][k] != 0) and (visited[k] == 0) :
          if tsp_g[c][k] < min_val:
             min_val = tsp_g[c][k]
             adj_vertex = k
  if min_val != 999:
      cost = cost + min_val
  if adj_vertex == 999:
     adj_vertex = 0
     print((adj_vertex + 1), end=" ")
     cost = cost + tsp_g[c][adj_vertex]
     return
  travellingsalesman(adj_vertex)
n = 5
cost = 0
visited = [0,0,0,0,0]
tsp_g = [[12, 30, 33, 10, 45],
                  [56, 22, 9, 15, 18],
                  [29, 13, 8, 5, 12],
                  [33, 28, 16, 10, 3],
                  [1, 4, 30, 24, 20]]
print("Shortest Path:", end=" ")
travellingsalesman(0)
print()
print("Minimum Cost:", end=" ")
print(cost)
