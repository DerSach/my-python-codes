#Codewars - 6 kyu
# You are going to be given an array of integers.
# Your job is to take that array and find an index N where the sum of the integers to the left of N is equal
# to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

def find_even_index(arr):
    numIndex = -1
    for i in arr:
        numIndex += 1
        leftValue = rightValue = 0
        for j in range(0,numIndex):
            leftValue += int(arr[j])
        for j in range (numIndex+1,len(arr)):
            rightValue += int(arr[j])
        if leftValue == rightValue:
            return numIndex
    return -1
