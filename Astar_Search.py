from queue import PriorityQueue
class State(object):
    def __init__(self,value,parent,start=0,goal=0):
              self.children=[]
              self.parent=parent
              self.value=value
              self.dist=0
              if parent:
                  self.start=parent.start
                  self.goal=parent.goal
                  self.path=parent.path[:]
                  self.path.append(value)
              else:
                  self.path=[value]
                  self.start=start
                  self.goal=goal
    def GetDistance(self):
          pass
    def CreateChildren(self):
          pass
class State_String(State):
          def __init__(self,value,parent,start=0,goal=0):
              super(State_String,self).__init__(value,parent,start,goal)
              self.dist=self.GetDistance()
          def GetDistance(self):
              if self.value==self.goal:
                  return 0
              dist=0
              if isinstance(self.goal,str):
                for i in range(len(self.goal)):
                  letter=self.goal[i]
                  dist+=abs(i-self.value.index(letter))
              return dist
          def CreateChildren(self):
              if not self.children:
                  for i in range(len(self.goal)-1):
                      val=self.value
                      val=val[:i]+val[i+1]+val[i]+val[i+2:]
                      child=State_String(val,self)
                      self.children.append(child)

class A_Star_Solver:
    def __init__(self,start,goal):
        self.path=[]
        self.visitedQueue=[]
        self.priorityQueue=PriorityQueue()
        self.start=start
        self.goal=goal
    def solve(self):            
      start_state=State_String(self.start,0,self.start,self.goal)
      count=0
      self.priorityQueue.put((0,count,start_state))
      while not self.path and self.priorityQueue.qsize():
          closestchild=self.priorityQueue.get()[2]
          closestchild.CreateChildren()
          self.visitedQueue.append(closestchild.value)
          for child in closestchild.children:
              if child.value not in self.visitedQueue:
                  count+=1
              if not child.dist:
                  self.path=child.path
                  break
              self.priorityQueue.put((child.dist,count,child))
      if not self.path:
          print("Goal is not possible!"+self.goal)
      return self.path
start1="programming"
goal="pgrogrammin"
print("Starting...")
a=A_Star_Solver(start1,goal)
a.solve()
for i in range(len(a.path)):
    print("{0}) {1}".format(i,a.path[i]))