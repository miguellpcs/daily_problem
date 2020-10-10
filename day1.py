def solution(arr,val): #O(n)
    if len(arr) < 2: # O(n)
        return False

    previous_numbers = {}

    for cur in arr: # O(n)
        if (val - cur) in previous_numbers.keys(): # O(1)
            return True 
        previous_numbers[cur] = True # O(n)
    return False

