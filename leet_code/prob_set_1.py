# Given an int array nums and an int target,
# find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.

def unique_pairs(nums, target):

    res = {}
    out = set()

    for index, value in enumerate(nums):
        if target - value in res:
            out.add((value, target-value))
        else:
            res[index]=value

    return len(out)

listy = [0,1,2,3,4]
print (listy[0])
del listy[0]
print (listy[0])

print ('ccbccbb' > 'bccbccbb')
# chars = [char for char in word]
# print (chars)

# print (unique_pairs([1, 1, 2, 3,9,5,7,8,7,0], 9))