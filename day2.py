def solution(arr):
    """
    Description: Given an array of integers, return a new array such
    that each element at index i of the new array is the product of all the numbers in the original array
    except the one at i.
    
    Input: List of numbers arr
    Output: List of numbers out

    Algorithm: 
    With arr = [x1,x2,...x(n-1),xn] let

    [1] list1 = [x1,x1*x2,x1*x2*x3, ... x1*x2*x3*...*x(n-1)*xn] # Productory of arr starting from the left
    [2] list2 = [xn,xn*x(n-1),...,xn*x(n-1)...*x3*x2*x1]  # Productory of arr starting from the right


    [3] pos1: list2[-2]           # Product of all but x1 (xn*x(n-1)*...*x3*x2)

    [4]
    pos2: list2[-3] * list1[0]    # Product of all but x2 (x1 * (xn*x(n-1)*...*x3) ) 
    pos3: list2[-4] * list1[1]    # Product of all but x3 ((x1*x2) * (xn*x(n-1)*...) ) 

    posk: list2[-k-3] * list1[k]  # Generalizing  
    
    [5]
    posn: list1[-2]               # Product of all but xn (x1*x2*x3*...*x(n-1))
    
    1 and 2 have linear time complexity because they pass only one time through the list, doing multiplications. They also have linear space complexity, cause they create 2 arrays of the same size as the input.
    3 and 5 have constant time complexity. Its just an assignment.
    4 has linear time complexity. Because it does (N-2) assignments.

    The algorithm has time complexity O(N) and space complexity O(n)


    """
    # All O(n)
    arr_size = len(arr)
    acc_1 = [arr[0]]
    acc_2 = [arr[arr_size-1]]
    out = []

    
    for idx in range(1,arr_size): # O(n)
        acc_1.append(arr[idx]*acc_1[-1])
    
    for idx in range(arr_size-2,-1,-1): # O(n)
        acc_2.append(arr[idx]*acc_2[-1])

    
    out.append(acc_2[-2])
    for idx in range(arr_size-2): # O(n)
        out.append(acc_2[-idx-3]*acc_1[idx])

    out.append(acc_1[-2])
   
    
    return out
    
   
    
def sol_with_division(arr):
    """
    Easy :P
    """
    acc = 1
    for val in arr:
        acc *= val

    out = [ int(acc/val) for val in arr]

    return out 


