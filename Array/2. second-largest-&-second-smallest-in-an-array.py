"""
Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	    Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	    Second Largest : -1
Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array.
             There is no second largest or second smallest element present.
"""

from typing import List

def getSecondLargest(array: List[int]) -> int:
    '''
    :type array: List[int]
    :rtype: int
    '''
    if (len(array) < 2):
        return -1

    largest = float('-inf')
    second_largest =  float('-inf')

    for i in range(len(array)):
        if array[i] > largest:
            largest, second_largest = array[i], largest
    
        elif(array[i] > second_largest and array[i] < largest):
            second_largest = array[i]
    
    return second_largest

def getSecondSmallest(array: List[int]) -> int:
    '''
    :type array: List[int]
    :rtype: int
    '''

    if (len(array) < 2):
        return -1
    
    smallest = float('inf')
    second_smallest = float('inf')

    for i in range(len(array)):
        if array[i] < smallest:
            smallest, second_smallest = array[i], smallest
        
        elif(array[i] < second_smallest and array[i] > smallest):
            second_smallest = array[i]
    
    return second_smallest

if __name__ == '__main__':
    print(getSecondLargest([1,2,4,7,7,5]))
    print(getSecondSmallest([1,2,4,7,7,5]))

    print(getSecondLargest([1]))
    print(getSecondSmallest([1]))

"""
Complexity:
Time Complexity: O(N), Single-pass solution
Space Complexity: O(1)
"""