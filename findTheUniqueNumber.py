#Codewars - 6 kyu
# Find the unique number in an array of at least 3 numbers
# Example: find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
