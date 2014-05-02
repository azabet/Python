"""
Merge Sort procedure for sorting an array.
"""

def Merge(a,b):
  """
  Usage: sorted_merged_array = merge(sorted_array1, sorted_array2)
  Merges two sorted arrays in a sorted fashion.
  """
  merged = []     ## merged array
  i = 0           ## counter for array a
  j = 0           ## counter for array b
  ## Scan through a and b and add the smaller elements to the merged array
  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      merged.append(a[i])
      i += 1
    else:
      merged.append(b[j])
      j += 1
  ## Add the leftovers to the merged array
  if i == len(a):  ## gone through a, add the rest of b
    merged += b[j:]
  else:
    merged += a[i:]  
  return(merged)

def MergeSort(a):
  """
  Sorts an array by recursively dividing it into two halves.
  """
  n = len(a)
  ## Base cases for n=1,2
  if n == 1:
    return(a)
  if n == 2:
    if a[0] > a[1]:
      a[0], a[1] = a[1], a[0]
    return(a)
  ## Recursive operation
  halfsize = n//2
  sorted = Merge(MergeSort(a[:halfsize]), MergeSort(a[halfsize:]))
  return(sorted)
  
def main():
  a = [6,8,1,9,4]
  print('Input array: ', a)
  b = MergeSort(a)
  print('Sorted array: ', b)
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
