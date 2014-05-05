"""
Dijkstra's algorithm for finding the shortest path in a graph.
Amir Zabet @ 05/04/2014
"""

import random

def Dijkstra(W,Start,Finish):
  """
  Usage: Shortest_Path = Dijkstra(Weight_Matrix, Start, Finish)
  Given a matrix for the weights of graph edges, finds the 
  shortest path between the Start and Finish vertices.
  """
  # define lists
  Visited = []   ## list of visited vertices
  SP = {}        ## shortest-path distances of visited vertices
  pred = {}      ## predecessors of visited vertices
  Unvisited = [] ## list of unvisited vertices
  d = []         ## distances of unvisited vertices from Start
  ## initialize
  Visited.append(Start)
  pred[Start] = Start
  SP[Start] = 0
  for j in range(len(W)):
    if not j == Start:
      Unvisited.append(j)
      d_ij = W[Start][j]
      d.append(d_ij)
      if d_ij < float("inf"):
        SP[j] = d_ij
        pred[j] = Start
  Current = Start ## current vertex
  Next = Start    ## next vertex
  while Unvisited and (not Next == Finish):
    ## find the nearest unvisited vertex and set it to Next
    d_min = min(d)
    index = d.index(min(d))
    Next = Unvisited[index]
    ## if Next is a new shortest path, update its attributes 
    if (not Next in SP) or (d_min < SP[Next]):
      SP[Next] = d_min
      pred[Next] = Current
    ## remove Next from Unvisited and add it to Visited
    Unvisited.pop(index) 
    d.pop(index)
    Visited.append(Next)
    ## update the distances of unvisited vertices
    for j in range(len(Unvisited)):
      u = Unvisited[j]
      new_SP = d_min + W[Next][u]
      ## if a new shortest-path is found, set Next as Current
      if new_SP < d[j]:
        d[j] = new_SP
        Current = Next
  ## end of while
  print('Shortest distance to every vertex:', [SP[i] for i in SP])
  ## backtrack the list of predecessors from Finish to Start
  path = [Visited[-1]]
  p = pred[Visited[-1]]
  while not p == Start:
    path = [p] + path
    p = pred[p]
  path = [Start] + path
  print('Start: ', Start)
  print('Finish: ', Finish)
  print('Shortest path:', path)
  print('Shortest distances:', [SP[i] for i in path])
  return(path,SP)
 
def main():
  N = 5   ## number of vertices
  ## define weights
  w = list(range(11))
  w[10] = float("inf")
  ## create a random matrix of weights for the graph edges
  W = [[w[random.randint(1,10)] for i in range(N)] for i in range(N)]
  for i in range(N):
    W[i][i] = ''
  ## print the graph
  print('Input graph:')
  print('  ', str(list(range(N)))[1:-1])  ## vertex label
  for i in range(N):
    print(i, W[i][:])
  Start = 0   ## Starting vertex
  Finish = 4  ## Finishing vertex
  Dijkstra(W,Start,Finish)
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
