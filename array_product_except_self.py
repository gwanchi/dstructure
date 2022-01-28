"""
Given an array of integers arr that has at least two elements, create a function that returns an array output where output[i] represents the product of all elements of arr except arr[i], and you are not allowed to use the division operator.
"""
def productExceptSelf(arr):
    n=len(arr)
    output=[]
    for i in range(len(arr)):
        productFromLeft = 1
        for j in range(i):
            productFromLeft *= arr[j]
        productFromRight = 1
        for j in range(n-1, i, -1):
            productFromRight *= arr[j]
        output.append(productFromLeft * productFromRight)
    return output

def productExceptSelf2(arr):
    n=len(arr)
    cumulativeFromLeft = [0]*n
    cumulativeFromLeft[0]=1
    for i in range(1,n):
        cumulativeFromLeft[i] = cumulativeFromLeft[i-1]*arr[i-1]
    cumumulativeFromRight = [0]*n
    cumumulativeFromRight[n-1]=1
    for i in range(n-2,-1-1):
        cumumulativeFromRight[i] = cumumulativeFromRight[i+1]*arr[i+1]
    output = [0]*n
    for i in range(n):
        output[i] = cumulativeFromLeft[i] * cumumulativeFromRight[i]
    return  output