def print_adjacency_list(adjacency_list):
 print 'Display adjacency list:'
 for i in range(len(adjacency_list)):
  print i,':',
  for j in range(len(adjacency_list[i])):
   print adjacency_list[i][j],
  print

def dijkstra(adjacency_list,src_node,dest_node):
 cur_distance=0
 cur_node=src_node
 node_queue.append((cur_node,cur_distance))
 visited_nodes.append(cur_node)
 while len(node_queue)!=0:
  any_node,min_dist=node_queue[0]
  ind=0
  mark=0
  for node in node_queue:
   if min_dist>node[1]:
    min_dist=node[1]
    mark=ind
   ind+=ind
  cur_node,cur_distance=node_queue.pop(mark)
  if cur_node!=dest_node:
   for neighbour in adjacency_list[cur_node]:
    next_distance=cur_distance
    if neighbour[0] not in visited_nodes:
     next_distance+=neighbour[1]
     flag_present=False
     if neighbour[0]!=dest_node:
      for node in node_queue:
       if neighbour[0]==node[0]:
        flag_present=True
        if next_distance<node[1]:
         node=(neighbour[0],next_distance)
      if not flag_present:
       node_queue.append((neighbour[0],next_distance))
     else:
      distance_array.append(next_distance)
  if cur_node not in visited_nodes:
   visited_nodes.append(cur_node)
 print 'Length of shortest path: ',min(distance_array)
   
adjacency_list=[[(1,1),(2,4)],[(0,1),(2,2),(3,5)],[(0,4),(1,2),(3,1)],[(1,5),(2,1)]]
print_adjacency_list(adjacency_list)

src_node=0
dest_node=3
node_queue=[]
visited_nodes=[]
distance_array=[]

dijkstra(adjacency_list,src_node,dest_node)