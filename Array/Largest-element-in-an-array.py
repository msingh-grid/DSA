"""
Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array. 
"""
from typing import List

def getLargest(array:List[int]) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    
    largest = array[0]
    for i in range(len(array)):
        if (array[i] > largest):
            largest = array[i]
    
    return largest

if __name__ == '__main__':
    print(getLargest([2,5,1,3,0]))
    print(getLargest([8,10,5,7,9]))