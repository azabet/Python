"""
A program to create a Max-Heap from an input array 
and then perform HeapSort.
Written by Amir Zabet, 5/1/2014
"""

import math

def Heap(a):
  """
  Usage: Heap(array)
  Converts array to a binary tree (Heap) and prints it.
  """
  for i in range(len(a)):
    if math.log(i+2,2) % 1 == 0:
      print(a[i])
    else:
      print(a[i], end=" ")
  print()
  return
  
def Max_Heapify(a,k):
  """
  Usage: Max_Heapified_array = Max_Heapify(array,node)
  Given an array and a node, creates a Max-Heap branch from that node.
  Note: node starts from 0.
  """
  left = 2*k+1        ## index of left child
  right = 2*k+2       ## index of right child
  if right < len(a):  ## both left and right children exist
    greater = k       ## assume parent is the greater element
    if a[greater] < a[left]:
      greater = left  ## left child is greater
    if a[greater] < a[right]:
      greater = right ## right child is greater
    if not greater == k:
      a[k], a[greater] = a[greater], a[k] ## swap the parent with the greater child
      a = Max_Heapify(a,greater)          ## run Max_Heapify on the swapped child
  elif left < len(a): ## only left child exists
    if a[k] < a[left]:
      a[k], a[left] = a[left], a[k]       ## swap the parent with the greater child
      ## No more operation needed
  return(a)

def Build_Max_Heap(a):
  """
  Usage: Max_Heap_array = Build_Max_Heap(array)
  Builds a Max-Heap tree from array.
  """
  n = len(a)-1
  if n==1:                          ## only two elements exist
    if a[0] < a[1]:                 ## compare the two elements
      a[0], a[1] = a[1], a[0]       
  else:
    index = range(math.floor(n/2))  ## only consider nodes less than n/2
    for i in index[::-1]:           ## start from the lowest level node
      a = Max_Heapify(a,i)          ## perform Max_Heapify on each node
  return(a)

def Min_Heapify(a,k):
  """
  Usage: Min_Heapified_array = Min_Heapify(array,node)
  Given an array and a node, creates a Min-Heap branch from that node.
  Note: node starts from 0.
  """
  left = 2*k+1        ## index of left child
  right = 2*k+2       ## index of right child
  if right < len(a):  ## both left and right children exist
    smaller = k       ## assume parent is the smaller element
    if a[smaller] > a[left]:
      smaller = left  ## left child is smaller
    if a[smaller] > a[right]:
      smaller = right ## right child is smaller
    if not smaller == k:
      a[k], a[smaller] = a[smaller], a[k] ## swap the parent with the smaller child
      a = Min_Heapify(a,smaller)          ## run Min_Heapify on the swapped child
  elif left < len(a): ## only left child exists
    if a[k] > a[left]:
      a[k], a[left] = a[left], a[k]       ## swap the parent with the smaller child
      ## No more operation needed
  return(a)

def Build_Min_Heap(a):
  """
  Usage: Min_Heap_array = Build_Min_Heap(array)
  Builds a Min-Heap tree from array.
  """
  n = len(a)-1
  if n==1:                          ## only two elements exist
    if a[0] > a[1]:                 ## compare the two elements
      a[0], a[1] = a[1], a[0]       
  else:
    index = range(math.floor(n/2))  ## only consider nodes less than n/2
    for i in index[::-1]:           ## start from the lowest level node
      a = Min_Heapify(a,i)          ## perform Min_Heapify on each node
  return(a)

def HeapSort(array):
  """
  Usage: sorted_array = HeapSort(array)
  Perform HeapSort on array.
  """
  a = array[:]
  sort = []
  while len(a)>1:
    a = Build_Min_Heap(a)
    sort.append(a[0])
    a[0], a[-1] = a[-1], a[0]
    del a[-1]
  sort.append(a[0])
  return(sort)
    
def main():
  a = [3,4,5,2,6,10,9]
  print('Input Array: ', a)
  b = HeapSort(a)
  print('Sorted Array: ', b)
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
