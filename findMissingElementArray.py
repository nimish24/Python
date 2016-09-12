__author__ = 'Nimish'

#### NOOB SOLUTION ####
def finder(arr1,arr2):
    for num in arr1:
        if num not in arr2:
            return num

##### SOLUTION 2 #####
'''
zip([1,2,3],[4,5,6]) = [ (1,4), (2,5), (3,6) ]
returns a list of tuples

'''
def finder2(arr1,arr2):
    arr1.sort()
    arr2.sort()

    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    return arr1[-1]

print finder([1,2,3,4,5,6,7],[3,4,6,2,1,7])
print finder2([1,2,3,4,5,6,7],[3,4,6,2,1,7])

#### SOLUTION 3 Using hash tables######
import collections

def finder3(arr1,arr2):
    d = collections.defaultdict(int) #if key is not in dictionary, then it adds it to the dictionary instead of giving an error

    for num in arr2:
        #count how many times no appears
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num

        else:
            d[num] -= 1

print finder3([1,2,3,4,5,6,7],[3,4,6,2,1,7])
