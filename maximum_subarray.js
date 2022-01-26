/*
Given an array of integers arr, create a function that returns the sum of the subarray that has the  greatest sum. And we don't consider the empty array as a subarray.
*/
function maximumSubarray(arr){
    let globalSum = -Infinity
    let localSum = 0
    for(let element of arr){
        localSum = Math.max(element, localSum + element)
        globalSum = Math.max(globalSum, localSum)
    }
    return globalSum;
}