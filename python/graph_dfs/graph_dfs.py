def set_adj_list(vertex_list,edge_list):
 for i in vertex_list:
  for j in vertex_list:
   if (i,j) in edge_list:
    adjacency_list[i].append(j)
    
def print_adj_list(adjacency_list):
 for i in range(len(adjacency_list)):
  print i,'->',adjacency_list[i]

def dfs(adjacency_list,node_start):
 node_stack.append(node_start)
 while len(node_stack)!=0:
  node_start=node_stack.pop()
  print node_start,
  for neighbour in adjacency_list[node_start]:
   if neighbour not in node_visited:
    node_visited.append(neighbour)
    dfs(adjacency_list,neighbour)

vertex_list=[0,1,2,3,4]
edge_list=[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4)]

adjacency_list=[[],[],[],[],[]]

set_adj_list(vertex_list,edge_list)
print_adj_list(adjacency_list)

node_start=0
node_stack=[]
node_visited=[]

dfs(adjacency_list,node_start)
