import numpy as np

def solution(arr1, arr2):
    
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    result = arr1 @ arr2
    answer = []
    
    for i in result:
        answer.append(i.tolist())
    
    return answer