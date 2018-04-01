
import sys

Nv = int(sys.stdin.readline())
Ne = int(sys.stdin.readline())

graph = []
verts = [0 for i in range(Nv)]

for i in range(Ne):
	edge = [int(x) for x in sys.stdin.readline().split()]
	graph.append(edge)

def dfs(graph,root_vertex):
	verts[root_vertex] = 1
	for edge in graph:
		if edge[0] == root_vertex and verts[edge[1]] == 0:
			verts[edge[1]] = 1
			dfs(graph,edge[1])
		elif edge[1] == root_vertex and verts[edge[0]] == 0:
			verts[edge[0]] = 1
			dfs(graph,edge[0])

loops = 0

for n,i in enumerate(verts):
	if i == 0:
		dfs(graph,n)
		loops += 1

print (loops)

#  function dfs(graph, root_vertex)
#     Mark root_vertex as "visited"
#     for each vertex v connected to root_vertex by an edge do
#         if v is not marked as "visited"
#             Mark v as "visited"
#             dfs(graph, v)
#         end if
#     end for
# end function