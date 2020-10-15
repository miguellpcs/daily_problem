def solution(arr):
    """
    Description:  Given an array of integers, find the first missing positive integer in linear time
    and constant space. In other words, find the lowest positive integer that does not exist in the array.
    The array can contain duplicates and negative numbers as well.



    Input: List of numbers arr
    Output: The lowest positive integer that does not exist in the array low

    If the array has size n, then the lowest positive integer that does not exist in the array surely is 
    at most (n+1), because:
        If the array contains all the first n positive integers, then it not contain (n+1), therefore, (n+1) is
        the first lowest positive integer that does not exist in the array.
        
        If the array does not contain all the first n positive integer numbers, then one of they is the lowest
        positive integer that does not exist in the array.
    
    So we'll use the array to mark which numbers from 0 to n exist in the array turning the numbers to negative.

    First we'll remove the negative numbers and the zeros, since they are non-positive and negative numbers will be used to mark 
    the numbers that exists in the array. 
    Then we iterate over the array and if we find one of the n first positive, then we'll multiply by -1 the value that has that number as index.
    At the end of the loop, all the first n positive numbers that exists in the array will be marked. We can verify if the 
    number exists in the array just by checking the value in its position in the array. For example, to check if 
    "2" exists in the array, we can just look if the 2nd value in the array is positive or negative.
    Finally, we iterate over the array, returning the position of the first positive number.

    The algorithm has linear time complexity since it iterates over the array 3 times.
    The algorithm has constant space complexity since it allocates a fixed size of memory. 


    """

    if len(arr) == 0: #O(n)
        return 1
    else:
        arr = [ val for val in arr if val > 0 ] #O(n)
        arr_size = len(arr) + 1 #O(n)
        arr.append(arr_size) #O(1)

        for idx in range(arr_size): #O(n)
            if abs(arr[idx]) < arr_size: #O(1)
                if arr[abs(arr[idx])-1] > -1: #O(1)
                    arr[abs(arr[idx])-1] = -arr[abs(arr[idx])-1] #O(1)
        for idx in range(arr_size):#O(n)
            if arr[idx] > 0:
                return (idx+1)
    
        