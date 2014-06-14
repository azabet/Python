"""
MinimumEditDistance finds the Levenshtein distance between two strings.
Amir Zabet @ 06/06/2014
"""

import numpy as np

def main():
  X = "Saturday"
  Y = "saturdays"
  print('X: ', X)
  print('Y: ', Y)
  n = len(X)+1
  m = len(Y)+1
  D = np.zeros((n,m), dtype=np.int8)  ## Distance Matrix
  T = D.copy()  ## Traceback Matrix
  ## Cost of deletion, insertion, and substitution
  deletion = 1
  insertion = 1
  substitution = [2,0]
  ## Calculate distance and traceback matrices
  for i in range(n):
    for j in range(m):
      if i==0:
        D[i,j] = j
        T[i,j] = 1
      elif j==0:
        D[i,j] = i
        T[i,j] = 1
      else:
        ins = D[i-1,j] + insertion
        dlt = D[i,j-1] + deletion
        sub = D[i-1,j-1] + substitution[X[i-1]==Y[j-1]]
        values = [ins, dlt, sub]
        D[i,j] = min(values)
        T[i,j] = values.index(min(values))+1
  T[0,0] = 0
  print('Distance Matrix:')
  print(D)
  print('Minimum Edit Distance: ' ,D[n-1,m-1])
  print()
  print('Traceback Matrix:')
  print(T)
  print()
  ops = ['.', 'i', 'd', 's']
  c = [[ops[i] for i in j] for j in T]
  for i in c:
    print(' '.join(i))
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
