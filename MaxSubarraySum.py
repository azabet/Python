"""
MaxSubarraySum finds a subarray that has the highest sum of elements.
Amir Zabet @ 07/30/2014
"""

import random

def MaxSubarray(a):
    """
    Usage: (subarray, sum) = MaxSubarray(a)
    """
    # Check if the array elements are all positive or all negative
    posCheck = [x >= 0 for x in a]
    negCheck = [x <= 0 for x in a]

    # If all positive, return the array
    if all(posCheck):
        return a, sum(a)

    # If all negative, return the maximum element
    if all(negCheck):
        return max(a), max(a)

    currentSum = a[0]
    currentSubarray = [a[0]]
    maxSum = a[0]
    maxSubarray = [a[0]]
    
    for x in a[1:]:
        currentSum += x
        currentSubarray.append(x)
        if currentSum < 0:
            # If current sum is negative,
            # then start a new subarray
            currentSum = 0
            currentSubarray = []
        elif currentSum > maxSum:
            # If current sum is larger than the max,
            # then store the current subarray as the maxSubarray
            maxSum = currentSum
            maxSubarray = currentSubarray[:]
    return maxSubarray, maxSum

def main():
    a = [random.randint(-10,10) for i in range(10)]
    print 'Input Array:', a
    print 'Max Subarray', MaxSubarray(a)[0]
    print 'Max Sum', MaxSubarray(a)[1]

if __name__ == '__main__':
  main()
