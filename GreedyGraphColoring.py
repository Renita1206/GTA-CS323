import time

def addEdge(graph, v, w):
	graph[v].append(w)
	graph[w].append(v)
	return graph

def greedyColoring(graph, V):
    result = [-1] * V
    result[0] = 0
    available = [False] * V
    
    for u in range(1, V):
        for i in graph[u]:
            if (result[i] != -1):
                available[result[i]] = True
    
        color = 0
        while color < V:
            if (available[color] == False): break
            color += 1
			
        
        result[u] = color
        for i in graph[u]:
            if (result[i] != -1):
                available[result[i]] = False
    
    for u in range(V):
        print("Vertex", u, " - Color", result[u])
    print("No of Colors: ", (max(result))+1)

# Driver Code
if __name__ == '__main__':
    
    graph = [[] for i in range(5)]
    graph = addEdge(graph, 0, 1)
    graph = addEdge(graph, 0, 2)
    graph = addEdge(graph, 1, 2)
    graph = addEdge(graph, 1, 3)
    graph = addEdge(graph, 2, 3)
    graph = addEdge(graph, 1, 4)
    graph = addEdge(graph, 3, 0)

    print("Coloring of graph using Greedy Coloring ")
    t1 = time.perf_counter()
    greedyColoring(graph, 5)
    t2 = time.perf_counter()
    print("Time elapsed: ", round((t2-t1) * 10**6) )
