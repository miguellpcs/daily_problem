def solution(arr,val):
    if len(arr) < 2:
        return False

    previous_numbers = {}
    
    for cur in arr:
        if (val - cur) in previous_numbers.keys():
            return True
        previous_numbers[cur] = True
    return False

