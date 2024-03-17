class Queue:
  def __init__(self):
    self.queue = []
  def enqueue(self,v):
    self.queue.append(v)
  def isempty(self):
    return(self.queue==[])
  def dequeue(self):
    v=None
    if not self.isempty():
      v=self.queue[0]
      self.queue=self.queue[1:]
    return v
  def __str__(self):
    return(str(self.queue))
def BFS(AList,start):
  visited={}
  for v in AList.keys():
    visited[v]=False
  q=Queue()
  q.enqueue(start)
  visited[start]=True
  while(not q.isempty()):
    curr=q.dequeue()
    for i in AList[curr]:
      if(not visited[i]):
        visited[i]=True
        q.enqueue(i)
  return visited

AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
result=BFS(AList,0)
for i in result:
  print(i,end=" ")