"""
QuickSelect finds the kth smallest element of an array in linear time.
Amir Zabet @ 05/08/2014
"""
import random

def Partition(a):
  """
  Usage: (left,pivot,right) = Partition(array)
  Partitions an array around a randomly chosen pivot such that 
  left elements <= pivot <= right elements.
  Running time: O(n)
  """
  ## Base cases
  if len(a)==1: 
    return([],a[0],[])
  if len(a)==2: 
    if a[0]<=a[1]:
      return([],a[0],a[1])
    else:
      return([],a[1],a[0])
  ## Choose a random pivot
  p = random.randint(0,len(a)-1)  ## the pivot index
  pivot = a[p]  ## the pivot value
  right = []    ## the right partition
  left = []     ## the left partition
  for i in range(len(a)):
    if not i == p:
      if a[i] > pivot:
        right.append(a[i])
      else:
        left.append(a[i])
  return(left, pivot, right)
  
def QuickSelect(a,k):
  """
  Usage: kth_smallest_element = QuickSelect(array,k)
  Finds the kth smallest element of an array in linear time.
  """
  (left,pivot,right) = Partition(a)
  if len(left)==k-1:   ## pivot is the kth smallest element
    result = pivot
  elif len(left)>k-1: ## the kth element is in the left partition
    result = QuickSelect(left,k)
  else:               ## the kth element is in the right partition
    result = QuickSelect(right,k-len(left)-1)
  return result
  
def main():
  N = 10;
  k = 4;
  a = [random.randint(1,100) for i in range(N)]
  print('Input array: ', a)
  print('k =', k)
  b = QuickSelect(a,k)
  print('kth smallest element: ', b)
        
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
