"""
QuickSort procedure for sorting an array.
Amir Zabet @ 05/04/2014
"""

import random

def Partition(a,p):
  """
  Usage: Partition(array, pivot)
  Partitions an array around a pivot such that the left elements <=
  and the right elements >= the pivot value.
  """
  pivot = a[p]  ## the pivot value
  right = []    ## the right partition
  left = []     ## the left partition
  for i in range(len(a)):
    if not i == p:
      if a[i] > pivot:
        right.append(a[i])
      else:
        left.append(a[i])
  left.append(pivot)
  return(left, right)

def QuickSort(a):
  """
  Usage: sorted_array = QuickSort(array)
  Sorts an array using the Randomized QuickSort algorithm.
  """
  if len(a) <= 1:
    return(a)
  if len(a) == 2:
    if a[0] > a[1]:
      a[0], a[1] = a[1], a[0]
    return(a)
  k = random.randint(1, len(a)-1)
  (left,right) = Partition(a,k)
  return QuickSort(left)+QuickSort(right)
  
def main():
  a = [6,8,1,9,5,4]
  print('Input array: ', a)
  b = QuickSort(a)
  print('Sorted array: ', b)
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
