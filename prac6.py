from collections import defaultdict
class Graph:
    def __init__(self,Nodes):
        self.N=Nodes
        self.graph=defaultdict(list)
    def add_edge(self,u,v):
        self.graph[u].append(v)
    def find_path(self,src,dest):
        visited=[False]*(self.N)
        queue=[]
        queue.append(src)
        visited[src]=True
        while queue:
            n=queue.pop(0)
            if n==dest:
                return True
            for i in self.graph[n]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
        return False
g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,2)
g.add_edge(1,0)
u=3;v=4
if g.find_path(u,v):
    print("There is a path from node %d to node %d" %(u,v))
else:
    
    print("There is a no path from node %d to node %d" %(u,v))
u=3;v=1
if g.find_path(u,v):
    print("There is a path from node %d to node %d" %(u,v))
else:
    
    print("There is a no path from node %d to node %d" %(u,v))
    
    










