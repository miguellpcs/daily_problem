def solution(arr,val): #O(n)
    """
    Description:  Given a list of numbers and a number k, 
    return whether any two numbers from the list add up to k.

    Input: List of numbers arr, Integer val
    Output: True or False

    This algorithm has linear complexity since for each number on the list it will verify if the number that 
    adds up to Val is a valid key on the dictionary of seen numbers. The second task takes constant time since
    the "in" operator is implement with hash tables to dictionaries. 


    """
    if len(arr) < 2: # O(n)
        return False

    previous_numbers = {}

    for cur in arr: # O(n)
        if (val - cur) in previous_numbers.keys(): # O(1)
            return True 
        previous_numbers[cur] = True # O(n)
    return False

