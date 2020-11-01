from collections import deque
def maxSlidingWindow(nums: [int], k: int) -> [int]:
    if len(nums) == 1:
        return nums
    window = deque()
    maxes = []
    size = len(nums)
    # window = nums[0:k]
    for i in range(k):
        window.append(nums[i])
    # window.append(nums[0:k])
    maxy = max(window)
    maxes.append(maxy)
    
    for i in range (0,size-k):
        # popped = window[0]
        # del window[0]
        popped = window.popleft()
        
        added = nums[i+k]
        window.append(added)
        
        if popped == maxy:
            maxy = max(window)
            maxes.append(maxy)
        else:
            if added > maxy:
                maxy = added
                maxes.append(maxy)
            else:
                maxes.append(maxy)
    return maxes

maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)