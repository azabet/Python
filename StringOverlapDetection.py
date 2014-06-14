"""
StringOverlapDetection finds the longest matching segment within two strings
using the Smith-Waterman algorithm.
Amir Zabet @ 06/07/2014
"""

import numpy as np

def main():
  X = "Saturday"
  Y = "saturdays"
  print('X: ', X)
  print('Y: ', Y)
  n = len(X)+1
  m = len(Y)+1
  H = np.zeros((n,m),dtype=np.int8)  ## Distance Matrix
  T = H.copy()  ## Traceback Matrix
  ## Matching score for deletion, insertion, and substitution
  deletion = -1
  insertion = -1
  substitution = [-2,1]
  ## Calculate matching score and traceback matrix
  for i in range(n):
    for j in range(m):
      if i==0:
        H[i,j] = 0
        T[i,j] = 0
      elif j==0:
        H[i,j] = 0
        T[i,j] = 0
      else:
        ins = H[i-1,j] + insertion
        dlt = H[i,j-1] + deletion 
        sub = H[i-1,j-1] + substitution[X[i-1]==Y[j-1]]
        values = [0, ins, dlt, sub]
        op = max(values)
        H[i,j] = op
        T[i,j] = values.index(op)
  ## Print H
  print('Distance Matrix:')
  print(H)
  Hmax = np.unravel_index(H.argmax(),H.shape) 
  print('Maximum: ', Hmax, H[Hmax])
  ## Print T
  print('Traceback Matrix:')
  print(T)
  dir = ['.', '<', '^', '\\']
  c = [[dir[i] for i in j] for j in T]
  for i in c:
    print(' '.join(i))
  ## Find traceback
  (i,j) = Hmax
  traceback = []
  dir = [(-1,0),(0,-1),(-1,-1)]
  while H[i,j]>0:
    traceback.append((i,j))
    values = [H[i-1,j], H[i,j-1], H[i-1,j-1]]
    step = dir[values.index(max(values))]
    i = i + step[0]
    j = j + step[1]
  ## Print traceback and overlap
  print('Traceback path: ', traceback)  
  overlap = [X[i[0]-1] for i in traceback][::-1]
  print('Overlap :', ''.join(overlap))  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
