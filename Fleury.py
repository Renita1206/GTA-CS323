from collections import defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.n = vertices
        self.graph = defaultdict(list)
        self.start = 0
        self.end = 0
        self.count=0
        self.edges = 0
        
    def addEdge(self, u, v):
        if(u>=self.n or v>=self.n):
            print("Invalid Output")
        else:
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.edges+=1

    def printGraph(self):
        for i in range(self.n):
            print(i,":",self.graph[i])
        print()
    
    def removeEdge(self, u, v):
        if(v in self.graph[u]):
            self.graph[u].remove(v)
            self.graph[v].remove(u)

    def dfsCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if(visited[i]==False):
                count = count + self.dfsCount(i, visited)
        return count

    def isValid(self, u, v):
        if(len(self.graph[u])==1):
            return True
        else:
            visited = [False]*(self.n)
            c1 = self.dfsCount(u, visited)

            self.removeEdge(u,v)

            visited = [False]*(self.n)
            c2 = self.dfsCount(v, visited)

            if(c1>c2):
                return False
            else:
                return True

    def FleuryAlgo(self, u):
        for v in self.graph[u]:
            if self.isValid(u,v):
                print("%d-%d " %(u,v))
                self.end = v
                self.count+=1
                self.removeEdge(u,v)
                self.FleuryAlgo(v)

    def  FleuryStart(self):
        u = 0
        for i in range(self.n):
            if(len(self.graph[u])%2==1):
                u = i
                break
        self.start = u
        self.FleuryAlgo(u)
        if(self.count==self.edges):
            if(self.start==self.end):
                print("Eulerian Trail")
            else:
                print("Eulerian Path")
        else:
            print(self.count, self.edges)
            print("No Eulerian Path or Trail")
        

vertices = int(input("Enter no. of vertices: "))
g = Graph(vertices)
while(1):
    print("Enter edges of vertice or enter -1 to exit")
    u = int(input())
    if(u==-1):
        break
    v = int(input())
    g.addEdge(u, v)
g.printGraph()
g.FleuryStart()