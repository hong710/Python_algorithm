
#   Write a function that takes in a non-empty array of distinct integers and an
#   integer representing a target sum. If any two numbers in the input array sum
#   up to the target sum, the function should return them in an array, in any
#   order. If no two numbers sum up to the target sum, the function should return
#   an empty array.

from re import A


array = [3,5,-4,8,11,1,-1,-6]
targetSum = 10
#solution 1 O(N^2)
def twoNumberSum(array, targetSum):
    # Write your code here.
    result= []
    for i in range(len(array)-1):
        for j in range (i+1, len(array)):
            if (array[i]+ array[j] ==targetSum):
                result.extend([array[i],array[j]]) 
    return result

#solution 2

def twoNumberSum2(array, targetSum):
    nums={}
    result=[]
    for i in range(0,len(array)):
        y= targetSum -array[i]
        if y in nums:
            result.extend([array[i],y])
        else:
            nums[array[i]]=True
    return result

print (twoNumberSum(array, targetSum))
print (twoNumberSum2(array, targetSum))

array.sort